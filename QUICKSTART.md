"""
Quick Start Guide - Armenian Sign Language Recognition

This file provides a quick reference for getting started with the project.
"""

# ============================================================================
# INSTALLATION (One-time setup)
# ============================================================================

# 1. Open Command Prompt or Terminal in the project directory

# 2. Install all dependencies:
# Windows:
#   pip install -r requirements.txt

# Linux/Mac:
#   pip install -r requirements.txt

# (Or use the run scripts: run.bat on Windows, ./run.sh on Linux/Mac)


# ============================================================================
# RUNNING THE APPLICATION
# ============================================================================

# Option 1: Run main.py directly
#   python main.py

# Option 2: Use runner scripts
#   Windows: run.bat
#   Linux/Mac: ./run.sh

# Option 3: Run the app module directly
#   python -m src.app


# ============================================================================
# PROJECT STRUCTURE & KEY FILES
# ============================================================================

"""
PROJECT LAYOUT:
├── main.py                    ← Run this to start!
├── requirements.txt           ← Dependencies
├── config/config.py           ← All settings & gesture mappings
├── src/
│   ├── app.py                 ← Main application
│   ├── sentence_builder.py    ← Converts gestures to words
│   ├── data_collection.py     ← Collect training data
│   └── train_model.py         ← Train LSTM model
├── utils/
│   ├── gesture_utils.py       ← Gesture classification
│   └── ui_utils.py            ← UI components
└── data/ & models/            ← Auto-created by training
"""

# ============================================================================
# AVAILABLE GESTURES & SHORTCUTS
# ============================================================================

"""
KEYBOARD SHORTCUTS During Runtime:
  'q'  →  Quit application
  'c'  →  Clear sentence
  's'  →  Speak sentence
  'u'  →  Undo last word

MOUSE BUTTONS:
  Click "RESET"  →  Clear sentence
  Click "SPEAK"  →  Speak sentence  
  Click "UNDO"   →  Undo last word

SUPPORTED GESTURES:
  1. FIST (all fingers folded) → Ո
  2. OPEN_PALM (all extended) → Ա
  3. PEACE (index & middle) → Ե
  4. THUMBS_UP → Հա
  5. THUMBS_DOWN → Ոչ
  6. STOP_HAND → Կ
  7. POINT_INDEX → Ի
  8. LOVE_HAND (thumb & pinky) → Ր
  9. OK_SIGN → Օ
"""


# ============================================================================
# TRAINING YOUR OWN MODEL (3 Simple Steps)
# ============================================================================

"""
STEP 1: Collect Training Data
   python src/data_collection.py
   
   - Make each gesture in front of camera
   - Press SPACE to capture (collect 50-100 samples per gesture)
   - Data saved to data/training_data.npy and data/training_labels.npy

STEP 2: Train Model
   python src/train_model.py
   
   - Trains an LSTM neural network
   - Shows accuracy and loss
   - Saves model to models/gesture_model.h5

STEP 3: Use Trained Model
   - Edit src/app.py (around line 100) 
   - Uncomment the LSTM model loading code
   - Replace the rule-based gesture classification with model predictions

See train_model.py for exact integration code!
"""


# ============================================================================
# CONFIGURATION & CUSTOMIZATION
# ============================================================================

"""
EASY CHANGES (in config/config.py):

1. Change camera resolution:
   FRAME_WIDTH = 1280  (try 640 for faster performance)
   FRAME_HEIGHT = 720  (try 480 for faster performance)

2. Adjust gesture detection sensitivity:
   MIN_DETECTION_CONFIDENCE = 0.7  (lower = more sensitive)

3. Change number of gestures to store:
   MAX_WORDS_IN_SENTENCE = 20  (max words in sentence)

4. Add more gestures:
   - Add new entry to ARMENIAN_WORDS dict
   - Add classification logic in gesture_utils.py

5. Adjust text-to-speech:
   TTS_RATE = 150  (words per minute)
   TTS_VOLUME = 0.9  (0.0 to 1.0)
"""


# ============================================================================
# TROUBLESHOOTING
# ============================================================================

"""
PROBLEM: "Cannot open webcam"
SOLUTION:
  - Check if camera is connected
  - Check if another app is using camera
  - Try CAMERA_INDEX = 1 in config.py

PROBLEM: Gestures not recognized well
SOLUTION:
  - Ensure good lighting (natural light best)
  - Make clear, distinct hand movements
  - Train your own model (see TRAINING section above)
  - Increase GESTURE_BUFFER_SIZE for stability

PROBLEM: Slow performance / Low FPS
SOLUTION:
  - Lower FRAME_WIDTH and FRAME_HEIGHT
  - Reduce GESTURE_BUFFER_SIZE
  - Close other applications
  - Try on a faster computer

PROBLEM: Text-to-speech not working
SOLUTION:
  - Windows: Usually works automatically
  - Linux: May need: apt-get install espeak
  - Mac: Usually works automatically
  
PROBLEM: Import errors
SOLUTION:
  - Make sure you're in the project directory
  - Run: pip install -r requirements.txt
  - Check that Python version is 3.8 or higher
"""


# ============================================================================
# WHAT'S HAPPENING UNDER THE HOOD?
# ============================================================================

"""
REAL-TIME PROCESSING PIPELINE:

1. CAMERA CAPTURE (30 FPS)
   ↓
2. HAND DETECTION (MediaPipe)
   ↓
3. EXTRACT FEATURES (21 points → distances, angles)
   ↓
4. CLASSIFY GESTURE (rule-based or ML model)
   ↓
5. SMOOTH PREDICTIONS (buffer last 5 frames)
   ↓
6. BUILD SENTENCE (accumulate confirmed words)
   ↓
7. RENDER UI (buttons, text, hand landmarks)
   ↓
8. TEXT-TO-SPEECH (speak the Armenian sentence)

All happens in ~33ms per frame!
"""


# ============================================================================
# NEXT STEPS
# ============================================================================

"""
BEYOND BASICS:

1. Train a custom LSTM model:
   - Collect more data: 500+ samples per gesture
   - Experiment with different architectures
   - Add data augmentation
   - See src/train_model.py

2. Add more gestures:
   - Define new hand positions
   - Add to ARMENIAN_WORDS in config.py
   - Add classification rules in gesture_utils.py
   - Train new model with more classes

3. Improve accuracy:
   - Use CNN instead of LSTM
   - Add temporal sequences (compare frames over time)
   - Use TensorFlow Lite for faster inference

4. Deploy to web/mobile:
   - Convert model to TensorFlow.js (for web)
   - Use TensorFlow Lite (for mobile)
   - Create REST API with Flask

5. Multi-hand support:
   - Process left and right hand separately
   - Combine gestures from both hands
   - Recognize complex two-handed signs

See README.md for detailed documentation!
"""
