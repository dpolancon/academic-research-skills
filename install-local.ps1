# install-local.ps1 - Automated Installer for Academic Research Skills (14-Skill Suite)
# Synchronizes local repo with Claude Desktop, Antigravity (global config), and workspace discovery mirrors.
# Supports live two-way wiring via NTFS Directory Junctions (default) or static file copying.

param(
    [ValidateSet("Junction", "Copy")]
    [string]$Mode = "Junction",
    [string]$WorkspaceDir
)

$claudeSkillsDir = "C:\Users\$env:USERNAME\AppData\Local\Claude\skills"
$agySkillsDir = "C:\Users\$env:USERNAME\.gemini\config\skills"
$agyConfigDir = "C:\Users\$env:USERNAME\.gemini\config"
$sourceDir = "C:\ReposGitHub\academic-research-skills"
$agentSkillsDir = "$sourceDir\.agents\skills"
$claudeWorkspaceSkillsDir = "$sourceDir\.claude\skills"

$skills = @(
    "academic-paper",
    "academic-paper-reviewer",
    "academic-pipeline",
    "advisor-reviewer",
    "deep-research",
    "econ-slides",
    "econ-write",
    "editor-jacobin-lat",
    "heterodox-economics-review",
    "irf-plotting",
    "latex-compilation",
    "PE-phd-committee",
    "prose-register-critic",
    "umass-applied-econometrics"
)

function Sync-SkillDirectory($srcDir, $destBaseDir, $skillName, $linkMode) {
    if (!(Test-Path $destBaseDir)) {
        New-Item -ItemType Directory -Force -Path $destBaseDir | Out-Null
    }
    $targetDir = Join-Path $destBaseDir $skillName

    if ($linkMode -eq "Junction") {
        if (Test-Path $targetDir) {
            $item = Get-Item $targetDir -Force
            if ($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) {
                # Already a junction
                return
            } else {
                Remove-Item -Path $targetDir -Recurse -Force
            }
        }
        New-Item -ItemType Junction -Path $targetDir -Target $srcDir | Out-Null
    } else {
        if (!(Test-Path $targetDir)) {
            New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
        }
        Copy-Item -Path "$srcDir\*" -Destination "$targetDir\" -Recurse -Force
    }
}

Write-Host "Syncing 14 skills across discovery targets (Mode: $Mode)..." -ForegroundColor Cyan

foreach ($skill in $skills) {
    $src = "$sourceDir\$skill"
    if (Test-Path $src) {
        Write-Host "  -> Installing $skill..."
        # 1. Global Antigravity config (always use Junction for live two-way learning)
        Sync-SkillDirectory $src $agySkillsDir $skill $Mode
        # 2. Global Claude Code / Desktop
        Sync-SkillDirectory $src $claudeSkillsDir $skill $Mode
        # 3. Workspace Antigravity mirror
        Sync-SkillDirectory $src $agentSkillsDir $skill $Mode
        # 4. Workspace Claude Code mirror
        Sync-SkillDirectory $src $claudeWorkspaceSkillsDir $skill $Mode
        # 5. Optional explicit external workspace (e.g. Obsidian vault)
        if ($WorkspaceDir -and (Test-Path $WorkspaceDir)) {
            $extAgentSkills = Join-Path $WorkspaceDir ".agents\skills"
            Sync-SkillDirectory $src $extAgentSkills $skill $Mode
        }
    } else {
        Write-Warning "Source directory not found for: $skill"
    }
}

# Ensure global Antigravity skills.json configuration
$skillsJsonPath = Join-Path $agyConfigDir "skills.json"
$skillsJsonContent = @{
    entries = @(
        @{ path = "C:/ReposGitHub/academic-research-skills" }
    )
} | ConvertTo-Json -Depth 5
$skillsJsonContent | Out-File $skillsJsonPath -Encoding utf8

Write-Host "`nSuccessfully installed all 14 skills ($Mode mode) to:" -ForegroundColor Green
Write-Host "  - Antigravity Global Config: $agySkillsDir"
Write-Host "  - Claude Code Global Skills:  $claudeSkillsDir"
Write-Host "  - Workspace .agents/skills:   $agentSkillsDir"
Write-Host "  - Workspace .claude/skills:   $claudeWorkspaceSkillsDir"
if ($WorkspaceDir) {
    Write-Host "  - Target Workspace .agents:   $WorkspaceDir\.agents\skills"
}
Write-Host "  - Antigravity skills.json:    $skillsJsonPath"