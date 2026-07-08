#!/usr/bin/env python
"""
Launcher Script - Run Armenian Sign Language Recognition in Fullscreen
"""

import cv2
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.app import main


def run_fullscreen():
    """Run the application in fullscreen mode"""
    
    print("\n" + "=" * 70)
    print("🇦🇲 ARMENIAN SIGN LANGUAGE RECOGNITION - FULLSCREEN MODE")
    print("=" * 70)
    print("\nStarting application in fullscreen mode...")
    print("\nPress 'F' to toggle fullscreen during runtime")
    print("Press 'q' to exit\n")
    
    main()


if __name__ == "__main__":
    run_fullscreen()
