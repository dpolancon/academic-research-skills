# scripts/sync-skills.ps1 - Bi-Directional Skill Sync & Conflict Prevention Harness
# Academic Research Skills (ARS) Suite

[CmdletBinding()]
param(
    [switch]$Check,
    [switch]$Pull,
    [switch]$Push,
    [string]$Skill,
    [string]$Description,
    [string]$Type = "LEARNING",
    [switch]$ReinstallJunctions,
    [string]$WorkspaceDir
)

$ErrorActionPreference = "Stop"
$repoRoot = "C:\ReposGitHub\academic-research-skills"
$globalSkillsDir = "$env:USERPROFILE\.gemini\config\skills"
$globalSkillsJson = "$env:USERPROFILE\.gemini\config\skills.json"
$registryFile = Join-Path $repoRoot "UPDATE_REGISTRY.md"

$allSkills = @(
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

function Write-Section($title) {
    Write-Host "`n=== $title ===" -ForegroundColor Cyan
}

function Test-JunctionStatus($baseDir) {
    if (!(Test-Path $baseDir)) {
        return @{ Status = "Missing"; Count = 0; Healthy = 0 }
    }
    $healthy = 0
    foreach ($s in $allSkills) {
        $p = Join-Path $baseDir $s
        if (Test-Path $p) {
            $item = Get-Item $p -Force
            if ($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) {
                $target = $item.Target
                if ($target -like "*$s*") {
                    $healthy++
                }
            }
        }
    }
    return @{ Status = "Present"; Count = $allSkills.Count; Healthy = $healthy }
}

function Install-JunctionWiring($targetBase) {
    if (!(Test-Path $targetBase)) {
        New-Item -ItemType Directory -Force -Path $targetBase | Out-Null
    }
    foreach ($s in $allSkills) {
        $src = Join-Path $repoRoot $s
        $dest = Join-Path $targetBase $s
        if (Test-Path $dest) {
            $item = Get-Item $dest -Force
            if ($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) {
                continue
            } else {
                Remove-Item -Path $dest -Recurse -Force
            }
        }
        New-Item -ItemType Junction -Path $dest -Target $src | Out-Null
        Write-Host "  [+] Wired $s -> $src" -ForegroundColor Green
    }
}

# --- Action: Reinstall / Verify Junctions ---
if ($ReinstallJunctions) {
    Write-Section "Reinstalling / Verifying Directory Junctions"
    Write-Host "Wiring global Antigravity brain ($globalSkillsDir)..." -ForegroundColor Yellow
    Install-JunctionWiring $globalSkillsDir

    # Ensure skills.json
    $jsonContent = @{
        entries = @(
            @{ path = "C:/ReposGitHub/academic-research-skills" }
        )
    } | ConvertTo-Json -Depth 5
    $jsonContent | Out-File $globalSkillsJson -Encoding utf8
    Write-Host "  [+] Global skills.json verified." -ForegroundColor Green

    if ($WorkspaceDir -and (Test-Path $WorkspaceDir)) {
        $wsDir = Join-Path $WorkspaceDir ".agents\skills"
        Write-Host "Wiring workspace ($wsDir)..." -ForegroundColor Yellow
        Install-JunctionWiring $wsDir
    }
    Write-Host "`nAll junctions verified and live." -ForegroundColor Green
    exit 0
}

# --- Action: Pull & Ingest Remote Changes ---
if ($Pull) {
    Write-Section "Safe Remote Ingest & Conflict Prevention"
    Set-Location $repoRoot
    
    # Check dirty state
    $status = git status --porcelain
    $hasUncommitted = [bool]($status)

    if ($hasUncommitted) {
        $stashName = "Auto-stash before remote sync [$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')]"
        Write-Host "Local uncommitted modifications detected. Shelving into stash..." -ForegroundColor Yellow
        git stash push -m $stashName
        Write-Host "Stashed: $stashName" -ForegroundColor Gray
    }

    Write-Host "Fetching and rebasing against origin/main..." -ForegroundColor Cyan
    git fetch origin
    $pullResult = git pull --rebase origin main

    if ($hasUncommitted) {
        Write-Host "Restoring local modifications..." -ForegroundColor Yellow
        $popResult = git stash pop 2>&1
        if ($LASTEXITCODE -ne 0) {
            Write-Warning "Conflict detected while re-applying local modifications!"
            Write-Warning "Run 'git status' and resolve marked conflicts before committing."
            exit 1
        } else {
            Write-Host "Local modifications restored cleanly without conflict." -ForegroundColor Green
        }
    }
    Write-Host "`nSync complete. Local repository is up to date." -ForegroundColor Green
    exit 0
}

# --- Action: Commit & Push Local Learnings ---
if ($Push) {
    Write-Section "Broadcasting Local Learnings & Updating Registry"
    Set-Location $repoRoot

    if (-not $Skill) {
        $Skill = Read-Host "Enter skill name (e.g., econ-slides, latex-compilation)"
    }
    if (-not $Description) {
        $Description = Read-Host "Enter learning/update summary"
    }
    if (-not $Skill -or -not $Description) {
        Write-Error "Skill and Description are required to log an update."
        exit 1
    }

    # Generate entry ID
    $dateStr = (Get-Date -Format "yyyy-MM-dd HH:mm")
    $regLines = Get-Content $registryFile
    $entryCount = ($regLines | Where-Object { $_ -match '\| `REG-' }).Count + 1
    $entryId = "REG-{0:D3}" -f $entryCount
    $hostName = $env:COMPUTERNAME

    # Append to UPDATE_REGISTRY.md
    $newRow = "| ``$entryId`` | $dateStr | ``$hostName`` | ``$Skill`` | ``$Type`` | $Description | Staged / Committed |"
    Add-Content -Path $registryFile -Value $newRow
    Write-Host "Added $entryId to $registryFile" -ForegroundColor Green

    # Stage and commit
    git add -A
    $commitMsg = "feat($Skill): $Description [host: $hostName]"
    git commit -m $commitMsg

    # Rebase and push
    Write-Host "Fetching and pulling remote with rebase..." -ForegroundColor Cyan
    git fetch origin
    git pull --rebase origin main
    
    Write-Host "Pushing to origin/main..." -ForegroundColor Cyan
    git push origin main

    Write-Host "`nSuccessfully recorded learning, committed, and pushed to remote origin/main!" -ForegroundColor Green
    exit 0
}

# --- Default Action: Check & Status Overview ---
Write-Section "ARS Skill Sync & Remote Status Check"
Set-Location $repoRoot

Write-Host "Fetching remote status from origin..." -ForegroundColor Gray
git fetch origin 2>$null

$branchStatus = git status -b --porcelain
$aheadBehind = git rev-list --left-right --count HEAD...origin/main
$counts = $aheadBehind -split "\s+"
$ahead = [int]$counts[0]
$behind = [int]$counts[1]

Write-Host "Local Branch: main"
Write-Host "  -> Commits ahead of origin/main:  $ahead" -ForegroundColor $(if ($ahead -gt 0) { "Yellow" } else { "Green" })
Write-Host "  -> Commits behind origin/main: $behind" -ForegroundColor $(if ($behind -gt 0) { "Magenta" } else { "Green" })

$dirty = git status --porcelain
if ($dirty) {
    Write-Host "`nUncommitted local modifications:" -ForegroundColor Yellow
    $dirty | ForEach-Object { Write-Host "   $_" }
} else {
    Write-Host "`nWorking directory: Clean" -ForegroundColor Green
}

Write-Section "Junction Wiring Health"
$globalJunc = Test-JunctionStatus $globalSkillsDir
Write-Host "Global Antigravity Brain ($globalSkillsDir):"
Write-Host "  -> Status: $($globalJunc.Status)"
Write-Host "  -> Active Wired Junctions: $($globalJunc.Healthy) / $($globalJunc.Count)" -ForegroundColor $(if ($globalJunc.Healthy -eq $globalJunc.Count) { "Green" } else { "Red" })

if ($WorkspaceDir) {
    $wsDir = Join-Path $WorkspaceDir ".agents\skills"
    $wsJunc = Test-JunctionStatus $wsDir
    Write-Host "Workspace Mirror ($wsDir):"
    Write-Host "  -> Active Wired Junctions: $($wsJunc.Healthy) / $($wsJunc.Count)" -ForegroundColor $(if ($wsJunc.Healthy -eq $wsJunc.Count) { "Green" } else { "Red" })
}

Write-Section "Recent Update Registry Entries"
if (Test-Path $registryFile) {
    Get-Content $registryFile | Where-Object { $_ -match '\| `REG-' } | Select-Object -Last 5 | ForEach-Object {
        Write-Host "  $_" -ForegroundColor Gray
    }
}

Write-Host "`nHelpful Commands:" -ForegroundColor Cyan
Write-Host "  .\sync.ps1 -Check                                  # Check sync & health status"
Write-Host "  .\sync.ps1 -Pull                                   # Safely pull remote changes (auto-stash)"
Write-Host "  .\sync.ps1 -Push -Skill <name> -Description <text> # Record learning & push to origin"
Write-Host "  .\sync.ps1 -ReinstallJunctions                     # Re-verify and repair all junctions`n"
