"""
🇦🇲 Armenian Sign Language Recognition System
Main Entry Point - Starts the Application

This is the simplified entry point. For advanced usage and project structure,
see the 'src/' directory and README.md

Real-time hand gesture detection and conversion to Armenian speech
Uses: OpenCV, MediaPipe, LSTM, pyttsx3
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the main application
from src.app import main

if __name__ == "__main__":
    main()


# Armenian words mapped to simple gestures
ARMENIAN_WORDS = {
    'FIST': 'Ո',           # "Vo" - Arm letter
    'OPEN_PALM': 'Ա',      # "Ayb" - Hello/Greeting  
    'PEACE': 'Ե',          # "Ech" - Good
    'THUMBS_UP': 'Հա',     # "Ha" - Yes
    'THUMBS_DOWN': 'Ոչ',   # "Och" - No
    'STOP_HAND': 'Կ',      # "Ka" - Stop
    'POINT_INDEX': 'Ի',    # "Ini" - Look/Point
    'LOVE_HAND': 'Ր',      # "Ra" - Love
    'OK_SIGN': 'Օ',        # "O" - Ok
}

# ============================================================================
# GESTURE CLASSIFICATION (Placeholder - Ready for ML upgrade)
# ============================================================================

def calculate_hand_features(landmarks):
    """
    Extract features from hand landmarks for gesture classification
    Returns a dictionary of calculated features
    
    UPGRADE PATH: Replace this with ML model predictions (LSTM/CNN)
    Input: MediaPipe 21 hand landmarks
    Output: Feature vector for gesture classification
    """
    
    if not landmarks:
        return None
    
    # Get coordinates (normalized 0-1)
    coords = np.array([[lm.x, lm.y, lm.z] for lm in landmarks])
    
    # Calculate distances between key finger points and palm center
    # Palm center is landmark 0
    palm = coords[0]
    
    # Finger tips: 4(thumb), 8(index), 12(middle), 16(ring), 20(pinky)
    finger_tips = coords[[4, 8, 12, 16, 20]]
    
    # Calculate distances from palm to each finger tip
    distances = np.linalg.norm(finger_tips - palm, axis=1)
    
    # Calculate angle between fingers (simplified)
    # This creates a feature vector that can be used for ML
    features = {
        'distances': distances,  # 5 distances (one per finger)
        'coords_flat': coords.flatten(),  # All 21 points flattened (63 values)
        'hand_size': np.max(distances),  # Overall hand spread
    }
    
    return features


def classify_gesture_rules(landmarks, handedness):
    """
    Rule-based gesture classification for Armenian sign language
    
    This uses simple distance-based rules. Replace with ML model:
    - Extract features with calculate_hand_features()
    - Pass to trained Neural Network (LSTM/CNN)
    - Return confidence scores for each gesture
    """
    
    if not landmarks:
        return None, 0.0
    
    features = calculate_hand_features(landmarks)
    distances = features['distances']
    
    # ARMENIAN SIGN LANGUAGE RULES
    
    # Gesture: FIST (all fingers folded - "Ո" letter)
    if np.mean(distances) < 0.15:
        return "FIST", 0.85
    
    # Gesture: OPEN_PALM (all fingers extended fully - "Ա" letter)
    if np.mean(distances) > 0.35 and distances.std() < 0.1:
        return "OPEN_PALM", 0.85
    
    # Gesture: PEACE (index and middle extended - "Ե" letter)
    if distances[1] > 0.28 and distances[2] > 0.28 and distances[0] < 0.15 and distances[3] < 0.15:
        return "PEACE", 0.80
    
    # Gesture: THUMBS_UP (thumb far, other folded - "Հա")
    if distances[0] > 0.4 and np.mean(distances[1:]) < 0.12:
        return "THUMBS_UP", 0.82
    
    # Gesture: THUMBS_DOWN (opposite of thumbs up)
    if distances[0] < 0.1 and np.mean(distances[1:]) > 0.35:
        return "THUMBS_DOWN", 0.80
    
    # Gesture: POINT_INDEX (only index finger extended - "Ի")
    if distances[1] > 0.35 and distances[2] < 0.15 and distances[3] < 0.15:
        return "POINT_INDEX", 0.78
    
    # Gesture: STOP_HAND (fingers spread medium, all extended - "Կ")
    if 0.2 < np.mean(distances) < 0.32 and distances.std() > 0.08:
        return "STOP_HAND", 0.75
    
    # Gesture: LOVE_HAND (pinky and thumb extended - "Ր" - Love)
    if distances[0] > 0.3 and distances[4] > 0.3 and np.mean(distances[1:3]) < 0.15:
        return "LOVE_HAND", 0.75
    
    # Gesture: OK_SIGN (thumb and index close, others extended - "Օ")
    if distances[0] < 0.08 and distances[1] < 0.08 and np.mean(distances[2:]) > 0.25:
        return "OK_SIGN", 0.75
    
    return None, 0.0


# ============================================================================
# SENTENCE BUILDER
# ============================================================================

class SentenceBuilder:
    """
    Combines recognized gestures into Armenian words and sentences
    """
    
    def __init__(self, max_words=10):
        self.words = []
        self.max_words = max_words
        self.last_gesture = None
        self.word_count_threshold = 2  # Minimum repetitions to accept a word
        self.gesture_buffer = deque(maxlen=self.word_count_threshold)
        self.last_word_time = 0
    
    def add_gesture(self, gesture):
        """
        Add detected gesture to buffer
        Only adds when gesture is repeated N times (filter noise)
        """
        if gesture is None:
            self.gesture_buffer.clear()
            return False
        
        if gesture == self.last_gesture:
            self.gesture_buffer.append(gesture)
        else:
            self.gesture_buffer.clear()
            self.last_gesture = gesture
            self.gesture_buffer.append(gesture)
        
        # Once gesture is confirmed, convert to Armenian word and add to sentence
        if len(self.gesture_buffer) == self.word_count_threshold:
            armenian_word = ARMENIAN_WORDS.get(gesture, gesture)
            
            if len(self.words) < self.max_words:
                self.words.append(armenian_word)
                self.last_word_time = time.time()
                print(f"✍️ Added: {armenian_word} ({gesture})")
            
            self.gesture_buffer.clear()
            return True
        
        return False
    
    def get_sentence(self):
        """Return current sentence as Armenian text string"""
        return " ".join(self.words)
    
    def speak_sentence(self):
        """Convert Armenian sentence to speech"""
        sentence = self.get_sentence()
        if sentence.strip():
            print(f"🔊 Speaking Armenian: {sentence}")
            tts_engine.say(sentence)
            tts_engine.runAndWait()
    
    def clear(self):
        """Clear the sentence"""
        self.words = []
        self.gesture_buffer.clear()
        self.last_gesture = None
        print("🗑️ Sentence cleared!")
    
    def undo_last_word(self):
        """Remove last added word"""
        if self.words:
            removed = self.words.pop()
            self.gesture_buffer.clear()
            print(f"⌫ Removed: {removed}")


# ============================================================================
# BUTTON CLASS FOR RESET
# ============================================================================

class Button:
    """
    Clickable button for screen interaction
    """
    
    def __init__(self, x, y, width, height, text, color=(255, 100, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.is_hovered = False
    
    def draw(self, frame):
        """Draw button on frame"""
        # Change color if hovered
        color = (0, 255, 0) if self.is_hovered else self.color
        
        # Draw rectangle
        cv2.rectangle(frame, (self.x, self.y), 
                     (self.x + self.width, self.y + self.height),
                     color, -1)
        
        # Draw border
        cv2.rectangle(frame, (self.x, self.y),
                     (self.x + self.width, self.y + self.height),
                     (255, 255, 255), 2)
        
        # Draw text
        text_size = cv2.getTextSize(self.text, cv2.FONT_HERSHEY_SIMPLEX, 
                                    0.6, 2)[0]
        text_x = self.x + (self.width - text_size[0]) // 2
        text_y = self.y + (self.height + text_size[1]) // 2
        
        cv2.putText(frame, self.text, (text_x, text_y),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    
    def is_clicked(self, x, y):
        """Check if button was clicked"""
        return (self.x <= x <= self.x + self.width and 
                self.y <= y <= self.y + self.height)
    
    def update_hover(self, x, y):
        """Update hover state"""
        self.is_hovered = self.is_clicked(x, y)


# ============================================================================
# MOUSE CALLBACK FOR BUTTON CLICKS
# ============================================================================

reset_button = None
sentence_builder = None

def mouse_callback(event, x, y, flags, param):
    """Handle mouse clicks"""
    global reset_button, sentence_builder
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if reset_button and reset_button.is_clicked(x, y):
            sentence_builder.clear()
    
    if event == cv2.EVENT_MOUSEMOVE:
        if reset_button:
            reset_button.update_hover(x, y)


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application loop with Armenian sign language recognition"""
    
    global reset_button, sentence_builder
    
    # Initialize camera
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    
    if not cap.isOpened():
        print("❌ Cannot open webcam")
        return
    
    # Initialize gesture buffer (for smoothing predictions)
    gesture_buffer = deque(maxlen=GESTURE_BUFFER_SIZE)
    sentence_builder = SentenceBuilder()
    
    # Create window and set mouse callback
    window_name = "Armenian Sign Language Recognition"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback)
    
    # Create reset button
    reset_button = Button(FRAME_WIDTH - 150, 10, 130, 50, "🗑️ RESET", 
                         color=(50, 50, 200))
    
    speak_button = Button(FRAME_WIDTH - 320, 10, 150, 50, "🔊 SPEAK",
                         color=(0, 180, 0))
    
    undo_button = Button(FRAME_WIDTH - 490, 10, 160, 50, "⌫ UNDO",
                        color=(200, 100, 0))
    
    # Display timing
    last_display_time = 0
    current_display_text = ""
    current_display_confidence = 0.0
    
    print("✅ Armenian Sign Language Recognition Started!")
    print("=" * 70)
    print("CONTROLS:")
    print("  • Make hand gestures to recognize Armenian letters")
    print("  • Click 'RESET' button to clear sentence")
    print("  • Click 'SPEAK' button to speak the sentence")
    print("  • Click 'UNDO' button to remove last word")
    print("  • Press 'q' to quit")
    print("=" * 70)
    print("\nARMENIAN GESTURES:")
    for gesture, armenian in ARMENIAN_WORDS.items():
        print(f"  {gesture:20s} → {armenian}")
    print("=" * 70)
    
    frame_count = 0
    fps_start_time = time.time()
    fps_text = "FPS: 0.0"
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Can't read frame")
                break
            
            # Flip frame for selfie view
            frame = cv2.flip(frame, 1)
            frame_count += 1
            h, w = frame.shape[:2]
            
            # Convert to RGB for MediaPipe
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)
            
            # Process detected hands
            detected_gesture = None
            gesture_confidence = 0.0
            
            if results.multi_hand_landmarks and results.multi_handedness:
                for hand_landmarks, handedness in zip(results.multi_hand_landmarks, 
                                                       results.multi_handedness):
                    # Draw hand landmarks on frame
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                        mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
                    )
                    
                    # Classify gesture
                    gesture, confidence = classify_gesture_rules(
                        hand_landmarks.landmark,
                        handedness.classification[0].label
                    )
                    
                    if gesture and confidence > gesture_confidence:
                        detected_gesture = gesture
                        gesture_confidence = confidence
                        
                        # Show gesture label on hand
                        cv2.putText(frame, f"{gesture} {confidence:.0%}",
                                   (50, 100),
                                   cv2.FONT_HERSHEY_SIMPLEX, 1.2, 
                                   (0, 255, 0), 3)
            
            # Update gesture buffer (for smoothing)
            if detected_gesture:
                gesture_buffer.append((detected_gesture, gesture_confidence))
            
            # Get most common gesture from buffer
            if gesture_buffer:
                gestures = [g[0] for g in gesture_buffer]
                most_common = max(set(gestures), key=gestures.count)
                avg_confidence = np.mean([g[1] for g in gesture_buffer])
                
                # Try to add to sentence
                if sentence_builder.add_gesture(most_common):
                    current_display_text = ARMENIAN_WORDS.get(most_common, most_common)
                    current_display_confidence = avg_confidence
                    last_display_time = time.time() * 1000
            
            # ================================================================
            # DRAW UI
            # ================================================================
            
            # Draw top info panel
            cv2.rectangle(frame, (0, 0), (w, 130), (0, 0, 0), -1)
            
            # Draw gesture history/current
            current_time = time.time() * 1000
            if current_time - last_display_time < DISPLAY_TIME:
                gesture_text = f"📍 Last: {current_display_text} ({current_display_confidence:.0%})"
                cv2.putText(frame, gesture_text, (10, 35),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
            
            # Display current sentence in Armenian
            sentence = sentence_builder.get_sentence()
            sentence_display = sentence if sentence else "[Start recognizing hand gestures]"
            
            # Split sentence if too long
            if len(sentence) > 50:
                words = sentence.split()
                line1 = " ".join(words[:len(words)//2])
                line2 = " ".join(words[len(words)//2:])
                cv2.putText(frame, f"📝 Sentence: {line1}", (10, 70),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
                cv2.putText(frame, line2, (10, 100),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
            else:
                cv2.putText(frame, f"📝 Sentence: {sentence_display}", (10, 70),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
            
            # FPS counter
            if frame_count % 10 == 0:
                fps = 10 / (time.time() - fps_start_time)
                fps_start_time = time.time()
                fps_text = f"FPS: {fps:.1f}"
            cv2.putText(frame, fps_text, (w - 150, 35),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            
            # Draw buttons
            reset_button.draw(frame)
            speak_button.draw(frame)
            undo_button.draw(frame)
            
            # Hint text at bottom
            cv2.putText(frame, "Make hand gestures to recognize Armenian letters | Press 'q' to quit",
                       (10, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
            
            # Display frame
            cv2.imshow(window_name, frame)
            
            # ================================================================
            # KEYBOARD INPUT
            # ================================================================
            
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q'):  # Quit
                print("\n👋 Exiting Armenian Sign Language Recognition...")
                break
            
            elif key == ord('c'):  # Clear sentence
                sentence_builder.clear()
            
            elif key == ord('s'):  # Speak sentence
                print("🎤 Speaking Armenian sentence...")
                sentence_builder.speak_sentence()
            
            elif key == ord('u'):  # Undo last word
                sentence_builder.undo_last_word()
    
    finally:
        # Cleanup
        cap.release()
        cv2.destroyAllWindows()
        hands.close()
        tts_engine.stop()
        print("✅ Application closed")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()