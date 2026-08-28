$ErrorActionPreference = 'Stop'
$Repo = Split-Path -Parent $PSScriptRoot
Set-Location $Repo
if (-not (Test-Path '.venv')) { py -3.11 -m venv .venv }
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -e '.[desktop,build]'
& .\.venv\Scripts\pyinstaller.exe --noconfirm --clean --windowed --name MTLineStickerStudio --collect-all PySide6 --paths src src\line_sticker_pipeline\ui.py
Write-Host 'Build output: dist\MTLineStickerStudio\MTLineStickerStudio.exe'
