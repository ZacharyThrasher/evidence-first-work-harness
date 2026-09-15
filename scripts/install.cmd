@echo off
setlocal
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1"
set "code=%ERRORLEVEL%"
echo.
if not "%code%"=="0" (
  echo EFWH installation failed with exit code %code%.
) else (
  echo EFWH installation complete.
)
if /I not "%CMDCMDLINE%"=="" pause >nul
exit /b %code%
