@echo off
cd /d "%~dp0"
start "Portfolio Server" /B python -m http.server 8000
timeout /t 2 /nobreak >nul
start http://localhost:8000
