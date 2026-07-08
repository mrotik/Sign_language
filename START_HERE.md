"""
🇦🇲 COMPLETE START GUIDE - Armenian Sign Language Recognition with Visual Alphabet
Latest Version with Full Alphabet Display
"""

print("""

╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║        🇦🇲  ARMENIAN SIGN LANGUAGE RECOGNITION - START HERE  🇦🇲             ║
║                      Full Alphabet Display System                            ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝


═══════════════════════════════════════════════════════════════════════════════
📋 WHAT YOU NEED TO KNOW
═══════════════════════════════════════════════════════════════════════════════

✅ Visual alphabet reference shows ALL 9 gestures
✅ Can view while using the app
✅ Can view standalone without app
✅ Detailed text guide available
✅ Screenshots showing hand positions
✅ Everything from your desktop!


═══════════════════════════════════════════════════════════════════════════════
🚀 QUICK START (3 EASY STEPS)
═══════════════════════════════════════════════════════════════════════════════

STEP 1: Install Dependencies
   Open Command Prompt or Terminal in the project folder
   
   Type: pip install -r requirements.txt
   
   (This takes 2-3 minutes, only do this once)


STEP 2: View the Alphabet (Optional but Recommended)
   Type: python view_alphabet.py
   
   → A full screen window opens showing all 9 gestures
   → Shows each gesture with Armenian letter
   → Shows how to perform each gesture
   → Press any key to close when done


STEP 3: Start the App
   Type: python main.py
   
   → Camera opens
   → You see the video feed + alphabet reference on right side
   → Try making hand gestures!


═══════════════════════════════════════════════════════════════════════════════
🎓 VIEWING OPTIONS FOR ARMENIAN ALPHABET
═══════════════════════════════════════════════════════════════════════════════

4 WAYS TO VIEW THE ALPHABET:

┌─────────────────────────────────────────────────────────────────────────────┐
│ OPTION 1: Full Screen Alphabet Viewer (BEST FOR LEARNING)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Command: python view_alphabet.py                                           │
│                                                                             │
│  What You See:                                                              │
│    • 3x3 grid of all 9 gestures                                             │
│    • Large Armenian letters (easy to read)                                  │
│    • How to perform each gesture                                            │
│    • Professional layout (1920x1080)                                        │
│                                                                             │
│  When to Use:                                                               │
│    ✓ First time learning gestures                                           │
│    ✓ Want to study without running main app                                 │
│    ✓ Need a clean reference                                                 │
│    ✓ Offline learning                                                       │
│                                                                             │
│  Duration: 2-5 minutes for learning                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│ OPTION 2: Side Panel During App (LIVE REFERENCE)                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Command: python main.py                                                    │
│                                                                             │
│  What You See:                                                              │
│    • Main video feed on left                                                │
│    • All 9 gestures listed on RIGHT side                                    │
│    • Each gesture → Armenian letter mapping                                 │
│    • Always visible while recording                                         │
│    • Interactive buttons (RESET, SPEAK, UNDO)                              │
│                                                                             │
│  When to Use:                                                               │
│    ✓ Regular use while recognizing gestures                                 │
│    ✓ Want to see reference while performing                                 │
│    ✓ Practice building sentences                                            │
│    ✓ Test your recognition                                                  │
│                                                                             │
│  Duration: Continuous while using                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│ OPTION 3: Full Screen Popup During App (DETAILED VIEW)                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  How to Access: During main.py, press 'a' key                              │
│                                                                             │
│  What You See:                                                              │
│    • Same as Option 1 (full 3x3 grid)                                       │
│    • Brief descriptions for each gesture                                    │
│    • Large, clear display                                                   │
│    • Full frame size                                                        │
│                                                                             │
│  When to Use:                                                               │
│    ✓ Need more detail while using app                                       │
│    ✓ Forgot how to perform a gesture                                        │
│    ✓ Want to compare your hand to reference                                 │
│    ✓ Difficult recognition - need to debug                                  │
│                                                                             │
│  How to Return: Press any key                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│ OPTION 4: Text Guide in Console (DETAILED DESCRIPTIONS)                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Command: python GESTURE_GUIDE.py                                           │
│                                                                             │
│  What You See:                                                              │
│    • Text descriptions of all 9 gestures                                    │
│    • How to perform each one step-by-step                                   │
│    • Visual ASCII representations                                           │
│    • Common mistakes to avoid                                               │
│    • Finger anatomy reference                                               │
│    • Learning tips                                                          │
│                                                                             │
│  When to Use:                                                               │
│    ✓ Reading detailed instructions                                          │
│    ✓ Unable to run video (no display)                                       │
│    ✓ Need step-by-step guide                                                │
│    ✓ Detailed studying                                                      │
│                                                                             │
│  Duration: 5-10 minutes reading                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════════════════
📚 RECOMMENDED LEARNING ORDER
═══════════════════════════════════════════════════════════════════════════════

BEGINNER (First Time):
  
  1️⃣  python GESTURE_GUIDE.py
      → Read all 9 gesture descriptions (10 min)
      → Understand how to perform each
      
  2️⃣  python view_alphabet.py
      → See visual layout of all gestures (5 min)
      → Study the grid format
      
  3️⃣  python main.py
      → Keep side panel visible for reference
      → Try each gesture slowly (15 min)


INTERMEDIATE (Getting Better):

  1️⃣  python main.py
      → Main app with side panel always visible
      → Build 5-word sentences
      → Press 'a' if you forget a gesture
      → Practice for 20-30 minutes
      

ADVANCED (Fluent):

  1️⃣  python main.py
      → No need for reference panel
      → Recognize gestures instantly
      → Build complex sentences
      → Speak in Armenian!


═══════════════════════════════════════════════════════════════════════════════
🎮 KEYBOARD SHORTCUTS DURING APP
═══════════════════════════════════════════════════════════════════════════════

While running 'python main.py':

┌──────────────────────────────────────────────────────────┐
│ KEY        ACTION                                         │
├──────────────────────────────────────────────────────────┤
│ 'a'    Show/Hide FULL ALPHABET REFERENCE                │
│        → Opens big 3x3 grid window                       │
│        → Press any key to close & return                 │
│        → Great when you're stuck                         │
│                                                          │
│ 'q'    QUIT the application                              │
│        → Closes camera and windows                       │
│        → Clean exit                                      │
│                                                          │
│ 'c'    CLEAR sentence                                    │
│        → Removes all words you've added                  │
│        → Start fresh                                     │
│                                                          │
│ 's'    SPEAK the sentence                                │
│        → Converts Armenian text to speech                │
│        → Hear it in Armenian language!                   │
│                                                          │
│ 'u'    UNDO (remove last word)                           │
│        → Deletes just the most recent gesture            │
│        → Useful if you made a mistake                    │
│                                                          │
└──────────────────────────────────────────────────────────┘

MOUSE BUTTONS (During App):

┌──────────────────────────────────────────────────────────┐
│ BUTTON         ACTION                                    │
├──────────────────────────────────────────────────────────┤
│ 🗑️ RESET      Clear all words in sentence               │
│ 🔊 SPEAK      Speak the Armenian sentence                │
│ ⌫ UNDO        Remove the last word added                 │
│                                                          │
└──────────────────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════════════════
🖼️ VISUAL LAYOUT OF OPTIONS
═══════════════════════════════════════════════════════════════════════════════

VIEW 1: Main App with Side Panel
────────────────────────────────

┌─────────────────────────────────────────────────────┐
│ 📹 CAMERA FEED     │  📖 ALPHABET REFERENCE      │
│                   │  ┌──────────────────────────┐ │
│ ┌──────────────┐   │  │ FIST        → Ո        │ │
│ │              │   │  │ OPEN_PALM   → Ա        │ │
│ │ Your hand    │   │  │ PEACE       → Ե        │ │
│ │ here →  🖐️  │   │  │ THUMBS_UP   → Հա       │ │
│ │              │   │  │ THUMBS_DOWN → Ոչ      │ │
│ │              │   │  │ STOP_HAND   → Կ        │ │
│ │              │   │  │ POINT_INDEX → Ի        │ │
│ │              │   │  │ LOVE_HAND   → Ր        │ │
│ │              │   │  │ OK_SIGN     → Օ        │ │
│ │              │   │  │ 📖 Press 'a' for full  │ │
│ └──────────────┘   │  └──────────────────────────┘ │
│                   │                               │
│ Sentence: ...     │                               │
│ [RESET][SPEAK][UNDO]                             │
└─────────────────────────────────────────────────────┘


VIEW 2: Full Alphabet Reference (Press 'a')
────────────────────────────────────

┌──────────────────────────────────────────────────────────────┐
│          Armenian Sign Language - Gesture Reference          │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│  │ FIST     │  │ OPEN     │  │ PEACE    │                  │
│  │ Letter:  │  │ PALM     │  │ Letter:  │                  │
│  │ Ո        │  │ Letter:  │  │ Ե        │                  │
│  │ Close    │  │ Ա        │  │ Index +  │                  │
│  │ fist     │  │ All fing │  │ middle   │                  │
│  │          │  │ extended │  │ out      │                  │
│  └──────────┘  └──────────┘  └──────────┘                  │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│  │ THUMBS   │  │ THUMBS   │  │ STOP     │                  │
│  │ UP       │  │ DOWN     │  │ HAND     │                  │
│  │ Letter:  │  │ Letter:  │  │ Letter:  │                  │
│  │ Հա       │  │ Ոչ       │  │ Կ        │                  │
│  ...                                                         │
│                                                              │
│ Hold each gesture for 1 second | Press 'q' to return       │
└──────────────────────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════════════════
💡 TIPS FOR SUCCESS
═══════════════════════════════════════════════════════════════════════════════

✓ USE THE SIDE PANEL
  • Keep reference visible while learning
  • Compare your hand to the listed gestures
  • Don't rely on memory - check panel!

✓ PRESS 'a' WHEN STUCK
  • Full screen view is more detailed
  • Larger letters easier to read
  • Good lighting helps see better

✓ CLEAR LIGHTING IS KEY
  • Natural daylight is best
  • Avoid harsh shadows
  • Position yourself in front of light source

✓ PRACTICE EACH GESTURE
  • Perform each one 5-10 times
  • Get your hand recognized before moving on
  • Build muscle memory

✓ TEXT GUIDE FOR DETAILS
  • python GESTURE_GUIDE.py gives exact steps
  • Read descriptions carefully
  • Follow the "How to Perform" section exactly

✓ START SLOW
  • Learn 3 gestures first
  • Then add 3 more
  • Finally learn last 3


═══════════════════════════════════════════════════════════════════════════════
❓ WHAT IF I CAN'T SEE THE ALPHABET?
═══════════════════════════════════════════════════════════════════════════════

PROBLEM: Side panel is not showing in main app
SOLUTION:
  ✓ Make sure your screen is wide enough (1280+ pixels)
  ✓ Try pressing 'a' to see full reference
  ✓ Read GESTURE_GUIDE.py instead
  ✓ Close and restart app: python main.py

PROBLEM: Can't read Armenian letters
SOLUTION:
  ✓ Zoom in on your monitor
  ✓ Use view_alphabet.py for larger display
  ✓ Read GESTURE_GUIDE.py for descriptions
  ✓ Adjust font settings if available

PROBLEM: Window is too small
SOLUTION:
  ✓ Press 'F6' or use mouse to drag window larger
  ✓ Try fullscreen mode: python run_fullscreen.py
  ✓ Use view_alphabet.py (already full screen)

PROBLEM: Text is blurry or hard to read
SOLUTION:
  ✓ Clean your monitor/screen
  ✓ Zoom in using Ctrl+Plus
  ✓ Use GESTURE_GUIDE.py in terminal (clearer text)
  ✓ Try on a different monitor


═══════════════════════════════════════════════════════════════════════════════
🚀 COMMAND REFERENCE
═══════════════════════════════════════════════════════════════════════════════

All Available Commands:

┌─────────────────────────────────────────────────────────────┐
│ python main.py                                              │
│ → Main app (camera + side alphabet panel)                  │
│ → Most common - what you'll use daily                      │
│                                                             │
│ python view_alphabet.py                                     │
│ → Full screen alphabet reference                           │
│ → Great for learning before using app                      │
│                                                             │
│ python GESTURE_GUIDE.py                                     │
│ → Text guide with detailed descriptions                    │
│ → Step-by-step instructions                                │
│                                                             │
│ python run_fullscreen.py                                    │
│ → App in fullscreen mode                                   │
│ → Better for large displays                                │
│                                                             │
│ run.bat (Windows) / run.sh (Linux/Mac)                     │
│ → Same as: python main.py                                  │
│ → Easy launcher scripts                                    │
│                                                             │
│ pip install -r requirements.txt                            │
│ → Initial setup only - install dependencies                │
│                                                             │
└─────────────────────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════════════════
📖 FILES CREATED FOR YOU
═══════════════════════════════════════════════════════════════════════════════

Documentation Files:
  📄 README.md                → Full technical documentation
  📄 QUICKSTART.md            → Quick reference
  📄 PROJECT_OVERVIEW.md      → Complete project structure  
  📄 NEW_FEATURES.md          → What's new in v2.0
  📄 GESTURE_GUIDE.py         → Detailed gesture guide
  📄 START_HERE.md            → This file!

Executable Scripts:
  🐍 main.py                  → Start here!
  🐍 view_alphabet.py         → View alphabet standalone
  🐍 run_fullscreen.py        → Fullscreen mode
  🐍 GESTURE_GUIDE.py         → Read gesture details
  💾 run.bat                  → Windows launcher
  💾 run.sh                   → Linux/Mac launcher

Source Code:
  📁 src/                     → Main application code
  📁 config/                  → Settings & mappings
  📁 utils/                   → Helper utilities
  📁 data/                    → Training data (created later)
  📁 models/                  → Trained models (created later)


═══════════════════════════════════════════════════════════════════════════════
🎉 YOU'RE READY TO START!
═══════════════════════════════════════════════════════════════════════════════

NEXT STEPS:

1. Open Terminal/Command Prompt in project folder

2. Install dependencies (ONE TIME ONLY):
   pip install -r requirements.txt

3. View the alphabet (optional):
   python view_alphabet.py

4. Start the app:
   python main.py

5. Try a gesture! 🖐️


═══════════════════════════════════════════════════════════════════════════════

Questions? Check the documentation files or press 'a' for alphabet help!

Good luck! 🇦🇲

═══════════════════════════════════════════════════════════════════════════════
""")
