#!/bin/bash
# Armenian Sign Language Recognition - Main Runner Script (Linux/Mac)

echo "════════════════════════════════════════════════════════════════════════════════"
echo "🇦🇲 ARMENIAN SIGN LANGUAGE RECOGNITION SYSTEM"
echo "════════════════════════════════════════════════════════════════════════════════"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "⚙️  Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "📦 Installing dependencies..."
pip install -r requirements.txt -q

# Run the application
echo "✅ Starting application..."
echo ""
python3 src/app.py
