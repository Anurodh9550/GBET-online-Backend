Set-Location $PSScriptRoot
$python = Join-Path $env:LOCALAPPDATA "gbt-api-venv\Scripts\python.exe"
& $python manage.py runserver 127.0.0.1:8000
