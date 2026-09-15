[CmdletBinding()]
param([switch]$Force)
$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Source = Join-Path $RepoRoot '.claude\skills\efwh'
$ConfigRoot = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $HOME '.claude' }
if ($ConfigRoot -match '^~[\\/]') { $ConfigRoot = Join-Path $HOME $ConfigRoot.Substring(2) }
$SkillsRoot = Join-Path $ConfigRoot 'skills'
$Destination = Join-Path $SkillsRoot 'efwh'
if (-not (Test-Path -LiteralPath (Join-Path $Source 'SKILL.md'))) { throw "EFWH source not found at $Source" }
if (Test-Path -LiteralPath $Destination) {
  if (-not $Force) { throw "EFWH is already installed at $Destination. Re-run with -Force to replace it." }
  $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
  $backup = "$Destination.backup-$stamp"
  Move-Item -LiteralPath $Destination -Destination $backup
  Write-Host "Backed up existing EFWH -> $backup"
}
New-Item -ItemType Directory -Force -Path $SkillsRoot | Out-Null
Copy-Item -LiteralPath $Source -Destination $Destination -Recurse
Write-Host "Installed EFWH 2.2.0 -> $Destination"
Write-Host "Start Claude Code in any workspace and run: /efwh <your problem>"
