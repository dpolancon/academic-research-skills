# install-local.ps1 - Automated Installer for Academic Research Skills (14-Skill Suite)
# Synchronizes local repo with Claude Desktop, Antigravity (global config), and workspace discovery mirrors.

$claudeSkillsDir = "C:\Users\$env:USERNAME\AppData\Local\Claude\skills"
$agySkillsDir = "C:\Users\$env:USERNAME\.gemini\config\skills"
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

# Helper function to reliably copy contents into target directory
function Sync-SkillDirectory($srcDir, $destBaseDir, $skillName) {
    $targetDir = Join-Path $destBaseDir $skillName
    if (!(Test-Path $targetDir)) {
        New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
    }
    # Copy all items directly into targetDir
    Copy-Item -Path "$srcDir\*" -Destination "$targetDir\" -Recurse -Force
}

Write-Host "Syncing 14 skills across all discovery targets..." -ForegroundColor Cyan

foreach ($skill in $skills) {
    $src = "$sourceDir\$skill"
    if (Test-Path $src) {
        Write-Host "  -> Installing $skill..."
        # 1. Global Antigravity config
        Sync-SkillDirectory $src $agySkillsDir $skill
        # 2. Global Claude Code / Desktop
        Sync-SkillDirectory $src $claudeSkillsDir $skill
        # 3. Workspace Antigravity mirror
        Sync-SkillDirectory $src $agentSkillsDir $skill
        # 4. Workspace Claude Code mirror
        Sync-SkillDirectory $src $claudeWorkspaceSkillsDir $skill
    } else {
        Write-Warning "Source directory not found for: $skill"
    }
}

Write-Host "`nSuccessfully installed all 14 skills to:" -ForegroundColor Green
Write-Host "  - Antigravity Global Config: $agySkillsDir"
Write-Host "  - Claude Code Global Skills:  $claudeSkillsDir"
Write-Host "  - Workspace .agents/skills:   $agentSkillsDir"
Write-Host "  - Workspace .claude/skills:   $claudeWorkspaceSkillsDir"