@echo off
REM Armenian Sign Language Recognition - Main Runner Script

echo ════════════════════════════════════════════════════════════════════════════════
echo 🇦🇲 ARMENIAN SIGN LANGUAGE RECOGNITION SYSTEM
echo ════════════════════════════════════════════════════════════════════════════════

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist venv (
    echo ⚙️  Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install requirements
echo 📦 Installing dependencies...
pip install -r requirements.txt -q

REM Run the application
echo ✅ Starting application...
echo.
python src/app.py

pause
