"""
Armenian Alphabet Reference - Full Display
Standalone script to view the full Armenian alphabet with gesture mappings
Run: python view_alphabet.py
"""

import cv2
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.alphabet_display import create_alphabet_template


def main():
    """Display the full Armenian alphabet reference"""
    
    print("\n" + "=" * 70)
    print("🇦🇲 ARMENIAN ALPHABET - FULL REFERENCE")
    print("=" * 70)
    print("\nShowing all 9 supported Armenian hand gestures and their meanings...")
    print("\nPress any key to close the window\n")
    
    # Create and display template
    template = create_alphabet_template(width=1920, height=1080)
    
    # Display in fullscreen or large window
    cv2.namedWindow("Armenian Alphabet Reference", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Armenian Alphabet Reference", template)
    
    print("📖 Window is now open. Press any key to close it...\n")
    
    # Wait for keypress
    key = cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
    print("✅ Window closed. Exiting...\n")


if __name__ == "__main__":
    main()
