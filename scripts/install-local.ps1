# scripts/install-local.ps1 - Safe Local Skill Discovery Installer for ARS
# Implements bounded, non-destructive NTFS Directory Junction wiring for Claude Code and Antigravity.

[CmdletBinding()]
param(
    [string[]]$TargetComponents = @('public-scholarship'),
    [ValidateSet('claude', 'antigravity', 'all')]
    [string]$Client = 'all',
    [switch]$DryRun,
    [switch]$Uninstall,
    [string]$ClaudeSkillDir,
    [string]$AntigravitySkillDir
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path

# Default client roots if not overridden
if (-not $ClaudeSkillDir) {
    $ClaudeSkillDir = "$env:USERPROFILE\.claude\skills"
}
if (-not $AntigravitySkillDir) {
    $AntigravitySkillDir = "$env:USERPROFILE\.gemini\config\skills"
}

# Supported component target mappings (Pilot envelope: public-scholarship only)
$ComponentTargets = @{
    'public-scholarship' = (Join-Path $repoRoot 'skills\dissemination\public-scholarship')
}

function Test-IsReparsePoint($path) {
    if (-not (Test-Path $path)) { return $false }
    $item = Get-Item -LiteralPath $path -Force
    return [bool]($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint)
}

function Get-JunctionTarget($path) {
    if (-not (Test-IsReparsePoint $path)) { return $null }
    $item = Get-Item -LiteralPath $path -Force
    return $item.Target
}

function Install-SingleJunction($name, $srcPath, $destDir, $clientLabel) {
    $destPath = Join-Path $destDir $name
    Write-Host "[$clientLabel] Evaluating junction: $name -> $srcPath" -ForegroundColor Cyan

    if (-not (Test-Path $srcPath)) {
        throw "Source skill path does not exist on disk: $srcPath"
    }

    $skillDoc = Join-Path $srcPath 'SKILL.md'
    if (-not (Test-Path $skillDoc)) {
        throw "Source directory missing required SKILL.md: $srcPath"
    }

    if (-not (Test-Path $destDir)) {
        if ($DryRun) {
            Write-Host "  [DryRun] Would create parent directory: $destDir" -ForegroundColor Yellow
        } else {
            New-Item -ItemType Directory -Path $destDir -Force | Out-Null
            Write-Host "  [+] Created parent directory: $destDir" -ForegroundColor Green
        }
    }

    if (Test-Path $destPath) {
        $isReparse = Test-IsReparsePoint $destPath
        if (-not $isReparse) {
            Write-Warning "Refusing to overwrite existing non-junction directory/file: $destPath"
            return @{ Status = 'COLLISION_REFUSED'; Path = $destPath }
        }

        $currentTarget = Get-JunctionTarget $destPath
        # Verify ARS ownership: target must be inside our repository root
        if ($currentTarget -notlike "$repoRoot*") {
            Write-Warning "Refusing to touch junction owned by external source: $destPath -> $currentTarget"
            return @{ Status = 'EXTERNAL_OWNERSHIP_REFUSED'; Path = $destPath }
        }

        # Check uninstall first before idempotence
        if ($Uninstall) {
            if ($DryRun) {
                Write-Host "  [DryRun] Would safely unlink junction: $destPath" -ForegroundColor Yellow
                return @{ Status = 'DRY_RUN_UNLINK'; Path = $destPath }
            } else {
                [System.IO.Directory]::Delete($destPath, $false)
                Write-Host "  [-] Safely unlinked junction: $destPath" -ForegroundColor Gray
                return @{ Status = 'UNLINKED_OK'; Path = $destPath }
            }
        }

        if ($currentTarget -eq $srcPath) {
            Write-Host "  [=] Junction already up to date: $destPath -> $srcPath" -ForegroundColor Green
            return @{ Status = 'IDEMPOTENT_OK'; Path = $destPath }
        }

        # Need to retarget existing ARS junction
        if ($DryRun) {
            Write-Host "  [DryRun] Would retarget junction: $destPath (was $currentTarget -> now $srcPath)" -ForegroundColor Yellow
            return @{ Status = 'DRY_RUN_RETARGET'; Path = $destPath }
        } else {
            [System.IO.Directory]::Delete($destPath, $false)
            New-Item -ItemType Junction -Path $destPath -Target $srcPath | Out-Null
            Write-Host "  [*] Retargeted junction: $destPath -> $srcPath" -ForegroundColor Green
            return @{ Status = 'RETARGETED_OK'; Path = $destPath }
        }
    } else {
        if ($Uninstall) {
            Write-Host "  [=] Nothing to uninstall at: $destPath" -ForegroundColor Gray
            return @{ Status = 'ALREADY_ABSENT'; Path = $destPath }
        }

        if ($DryRun) {
            Write-Host "  [DryRun] Would create junction: $destPath -> $srcPath" -ForegroundColor Yellow
            return @{ Status = 'DRY_RUN_CREATE'; Path = $destPath }
        } else {
            New-Item -ItemType Junction -Path $destPath -Target $srcPath | Out-Null
            Write-Host "  [+] Created junction: $destPath -> $srcPath" -ForegroundColor Green
            return @{ Status = 'CREATED_OK'; Path = $destPath }
        }
    }
}

$results = @()
foreach ($comp in $TargetComponents) {
    if (-not $ComponentTargets.ContainsKey($comp)) {
        Write-Warning "Component '$comp' is not recognized in authorized installation manifest."
        continue
    }
    $targetDir = $ComponentTargets[$comp]

    if ($Client -eq 'claude' -or $Client -eq 'all') {
        $results += Install-SingleJunction $comp $targetDir $ClaudeSkillDir 'Claude Code'
    }
    if ($Client -eq 'antigravity' -or $Client -eq 'all') {
        $results += Install-SingleJunction $comp $targetDir $AntigravitySkillDir 'Antigravity'
    }
}

Write-Host "`nInstallation operation finished. Summary:" -ForegroundColor Cyan
$results | Format-Table -AutoSize
