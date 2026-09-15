[CmdletBinding()]
param([switch]$PurgeExisting)
$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Source = Join-Path $RepoRoot '.claude\skills\efwh'
$ConfigRoot = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $HOME '.claude' }
if ($ConfigRoot -match '^~[\\/]') { $ConfigRoot = Join-Path $HOME $ConfigRoot.Substring(2) }
$SkillsRoot = Join-Path $ConfigRoot 'skills'
$Destination = Join-Path $SkillsRoot 'efwh'

function Get-TreeDigest([string]$Path) {
  $sha = [System.Security.Cryptography.SHA256]::Create()
  try {
    $files = Get-ChildItem -LiteralPath $Path -Recurse -File | Sort-Object FullName
    foreach ($file in $files) {
      $relative = $file.FullName.Substring($Path.Length).TrimStart('\\','/').Replace('\\','/')
      $nameBytes = [Text.Encoding]::UTF8.GetBytes($relative + "`0")
      $sha.TransformBlock($nameBytes,0,$nameBytes.Length,$null,0) | Out-Null
      $bytes = [IO.File]::ReadAllBytes($file.FullName)
      $sha.TransformBlock($bytes,0,$bytes.Length,$null,0) | Out-Null
      $zero = [byte[]](0)
      $sha.TransformBlock($zero,0,1,$null,0) | Out-Null
    }
    $sha.TransformFinalBlock([byte[]]::new(0),0,0) | Out-Null
    return ([BitConverter]::ToString($sha.Hash)).Replace('-','').ToLowerInvariant()
  } finally { $sha.Dispose() }
}

if (-not (Test-Path -LiteralPath (Join-Path $Source 'SKILL.md'))) { throw "EFWH source not found at $Source" }
$sourceHash = Get-TreeDigest $Source
if (Test-Path -LiteralPath $Destination) {
  if ((Get-TreeDigest $Destination) -eq $sourceHash) {
    Write-Host "EFWH 2.3.0 is already installed and verified at $Destination"
    exit 0
  }
  if ($PurgeExisting) {
    Remove-Item -LiteralPath $Destination -Recurse -Force
  } else {
    $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $backup = "$Destination.backup-$stamp"
    Move-Item -LiteralPath $Destination -Destination $backup
    Write-Host "Backed up existing EFWH -> $backup"
  }
}
New-Item -ItemType Directory -Force -Path $SkillsRoot | Out-Null
Copy-Item -LiteralPath $Source -Destination $Destination -Recurse
if ((Get-TreeDigest $Destination) -ne $sourceHash) { throw 'EFWH verification failed after copy.' }
Write-Host "Installed and verified EFWH 2.3.0 -> $Destination"
Write-Host "Start Claude Code anywhere and run: /efwh <your problem>"
