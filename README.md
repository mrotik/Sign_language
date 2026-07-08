# Armenian Sign Language Recognition System

A complete Python project for real-time Armenian Sign Language recognition using:
- **OpenCV**: Webcam access and frame processing
- **MediaPipe**: Hand landmark detection (21 key points per hand)
- **LSTM Neural Networks**: Gesture classification (trainable)
- **Text-to-Speech**: pyttsx3 for speaking Armenian text

## 📋 Project Structure

```
diplom/
├── src/                          # Main application code
│   ├── app.py                   # 🚀 Main application (run this!)
│   ├── sentence_builder.py      # Converts gestures to Armenian words
│   ├── data_collection.py       # Collect training data
│   ├── train_model.py           # Train LSTM model
│   └── __init__.py
│
├── config/                       # Configuration files
│   ├── config.py                # All settings and Armenian alphabet mapping
│   └── __init__.py
│
├── utils/                        # Utility modules
│   ├── gesture_utils.py         # Gesture classification logic
│   ├── ui_utils.py              # UI drawing functions
│   └── __init__.py
│
├── data/                         # Training data (created during data collection)
│   ├── training_data.npy        # Feature vectors
│   └── training_labels.npy      # Gesture labels
│
├── models/                       # Trained models
│   └── gesture_model.h5         # Trained LSTM model (created after training)
│
├── requirements.txt              # Python dependencies
├── run.bat                       # Run on Windows
├── run.sh                        # Run on Linux/Mac
└── README.md                     # This file
```

## 🚀 Quick Start

### 1️⃣ Install Dependencies

**Windows:**
```bash
pip install -r requirements.txt
```

**Windows (with virtual environment):**
```bash
run.bat
```

**Linux/Mac:**
```bash
./run.sh
```

### 2️⃣ Run the Application

```bash
python src/app.py
```

## 🎮 How to Use

1. **Make hand gestures** in front of the camera
2. **Hold the gesture** for ~1 second to confirm
3. **Watch** Armenian words build up in the sentence (top of screen)
4. **Click buttons** to:
   - 🗑️ **RESET** - Clear the sentence
   - 🔊 **SPEAK** - Hear the sentence in Armenian
   - ⌫ **UNDO** - Remove last word
5. **Press 'q'** to exit

## 📍 Supported Armenian Gestures

| Gesture Name | Hand Position | Armenian Letter | Meaning |
|-------------|--------------|-----------------|---------|
| **FIST** | All fingers folded | Ո | - |
| **OPEN_PALM** | All fingers extended | Ա | Hello/Greeting |
| **PEACE** | Index & middle extended | Ե | Good |
| **THUMBS_UP** | Thumb up, others folded | Հա | Yes |
| **THUMBS_DOWN** | Thumb down, others extended | Ոչ | No |
| **STOP_HAND** | All fingers spread | Կ | Stop |
| **POINT_INDEX** | Only index extended | Ի | Look/Point |
| **LOVE_HAND** | Thumb & pinky extended | Ր | Love |
| **OK_SIGN** | Thumb & index close | Օ | Ok |

## 🧠 Training Your Own Model

### Step 1: Collect Training Data

```bash
python src/data_collection.py
```

This will:
- Ask you to perform each gesture
- Press SPACE to capture samples (collect 50-100 per gesture)
- Save data to `data/training_data.npy` and `data/training_labels.npy`

### Step 2: Train the LSTM Model

```bash
python src/train_model.py
```

This will:
- Load the collected training data
- Train an LSTM neural network
- Save the model to `models/gesture_model.h5`

### Step 3: Use the Trained Model

Edit `src/app.py` and replace the `classify_gesture_rules()` function with:

```python
from tensorflow.keras.models import load_model

model = load_model('models/gesture_model.h5')

def classify_gesture_rules(landmarks, handedness=None):
    if not landmarks:
        return None, 0.0
    
    features = calculate_hand_features(landmarks)
    features_array = features['coords_flat'].reshape(1, -1)
    
    predictions = model.predict(features_array, verbose=0)
    gesture_idx = np.argmax(predictions)
    confidence = np.max(predictions)
    
    gesture_list = list(ARMENIAN_WORDS.keys())
    gesture = gesture_list[gesture_idx]
    
    return gesture, float(confidence)
```

## ⚙️ Configuration

Edit `config/config.py` to customize:

- **Camera settings**: resolution, FPS
- **MediaPipe settings**: detection confidence, hand tracking smoothness
- **Gesture recognition**: buffer size, word detection threshold
- **TTS settings**: speech rate, volume
- **Model settings**: LSTM units, dropout rate, training epochs

## 🐛 Troubleshooting

### "Cannot open webcam"
- Check if camera is connected and not in use by another app
- Try changing `CAMERA_INDEX` in config.py (0, 1, 2...)

### Poor gesture recognition
- Ensure good lighting
- Make clear, distinct hand gestures
- Increase `GESTURE_BUFFER_SIZE` for more stability
- Collect and train your own model (see above)

### Slow performance
- Lower `FRAME_WIDTH` and `FRAME_HEIGHT` in config.py
- Reduce `GESTURE_BUFFER_SIZE`
- Close other applications

## 📚 Project Features

✅ Real-time hand detection with 21 landmarks  
✅ Support for Armenian alphabet  
✅ Interactive button-based UI  
✅ Text-to-speech synthesis  
✅ Gesture buffering for noise reduction  
✅ Modular, well-organized code  
✅ ML-ready architecture for LSTM/CNN training  
✅ Data collection pipeline  
✅ Training script included  

## 🔮 Future Improvements

- [ ] CNN-based gesture classification
- [ ] Sequence learning for multi-hand gestures
- [ ] Support for other sign languages
- [ ] Real-time model training
- [ ] GUI for easier data collection
- [ ] Export recognized text to file
- [ ] Web interface

## 📄 License

MIT License - Feel free to use and modify!

## 👨‍💻 Author

Created as a diploma/thesis project for Armenian Sign Language Recognition

---

**Need help?** Check the code comments for detailed explanations!

Happy signing! 🖐️🇦🇲
