# AI Doctor with Vision and Voice 🏥

A conversational AI medical assistant that combines vision (image analysis), voice (speech-to-text), and natural language processing to provide medical insights. This project uses Gradio for the web interface and multiple AI APIs to deliver a seamless doctor-patient interaction simulation.

## 🌟 Features

- **Voice Input**: Record patient queries directly from the microphone
- **Medical Image Analysis**: Upload and analyze medical images using advanced vision models
- **AI-Powered Responses**: Get detailed medical insights using Groq's LLaMA model
- **Voice Output**: Listen to AI doctor responses through text-to-speech conversion
- **Web Interface**: User-friendly Gradio-based interface accessible via browser
- **Real-time Processing**: Instant transcription and analysis with streaming responses

## 📋 Prerequisites

- **Python 3.13+** (project uses Python 3.13)
- **Microphone** (for voice recording)
- **API Keys**:
  - [Groq API Key](https://console.groq.com/) - For LLaMA model access and speech-to-text
  - [ElevenLabs API Key](https://www.elevenlabs.io/) - For high-quality voice synthesis
- **Internet Connection** - Required for API calls and model inference

## 🚀 Installation

### 1. Clone or Setup the Project

```bash
cd c:\Users\HP ENVY\Desktop\ai_voicebot
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

Using pip:
```bash
pip install -r requirements.txt
```

Or using Pipenv:
```bash
pipenv install
```

Required packages:
- `groq` - Groq API client
- `gradio` - Web UI framework
- `elevenlabs` - Text-to-speech synthesis
- `gtts` - Google Text-to-Speech (fallback)
- `pygame` - Audio playback
- `pydub` - Audio processing
- `speechrecognition` - Speech recognition
- `pyaudio` - Audio input/output
- `ffmpeg` - Audio/video processing

### 4. Set Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

Or set them in your system environment variables:

**Windows PowerShell:**
```powershell
$env:GROQ_API_KEY = "your_groq_api_key_here"
$env:ELEVENLABS_API_KEY = "your_elevenlabs_api_key_here"
```

## 📖 Usage

### Start the Application

```bash
python gradio_app.py
```

The application will start on: **http://127.0.0.1:7860**

### Using the Interface

1. **Record Audio**: Click on the microphone icon and speak your medical query
   - The app will automatically transcribe your speech to text
   
2. **Upload Image** (Optional): Upload a medical image for analysis
   - Supported formats: JPG, PNG, etc.
   - Images are analyzed along with your verbal query
   
3. **Submit**: Click the "Submit" button to process
   
4. **View Results**:
   - **Speech to Text**: Your recorded question transcribed
   - **Doctor's Response**: AI-generated medical insight
   - **Audio Response**: Listen to the doctor's response as voice

## 📁 Project Structure

```
ai_voicebot/
├── gradio_app.py              # Main Gradio UI application
├── brain_of_doctor.py         # Image analysis and LLaMA model integration
├── voice_of_the_patient.py    # Audio recording and speech-to-text
├── voice_of_the_doctor.py     # Text-to-speech synthesis
├── .env                       # Environment variables (keep secret!)
├── .gitignore                 # Git ignore rules
├── Pipfile                    # Pipenv dependencies
├── Pipfile.lock               # Locked dependency versions
├── README.md                  # This file
└── .venv/                     # Virtual environment
```

## 🔧 File Descriptions

### `gradio_app.py`
Main entry point for the application. Creates the Gradio interface with audio and image inputs, orchestrates the workflow, and displays results.

**Key Function:**
- `process_inputs(audio_filepath, image_filepath)` - Main processing pipeline

### `brain_of_doctor.py`
Handles medical image analysis using Groq's vision models.

**Key Functions:**
- `encode_image(image_path)` - Converts image to base64 for API transmission
- `analyze_image_with_query(query, model, encoded_image)` - Analyzes image with LLaMA model

**Model Used:** `meta-llama/llama-4-maverick-17b-128e-instruct`

### `voice_of_the_patient.py`
Handles audio recording and speech-to-text transcription.

**Key Functions:**
- `record_audio(file_path, timeout, phrase_time_limit)` - Records audio from microphone
- `transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY)` - Transcribes audio using Groq's Whisper model

**STT Model:** `whisper-large-v3`

### `voice_of_the_doctor.py`
Handles text-to-speech synthesis for AI doctor responses.

**Key Functions:**
- `text_to_speech_with_gtts(input_text, output_filepath)` - Uses Google TTS (with autoplay)
- `text_to_speech_with_elevenlabs(input_text, output_filepath)` - Uses ElevenLabs TTS (with autoplay)

**Voice ID (ElevenLabs):** `21m00Tcm4TlvDq8ikWAM`

## 🔄 How It Works

```
User Input (Audio + Image)
        ↓
1. Audio Recording & Transcription
   └─→ voice_of_the_patient.py
   └─→ Converts speech to text using Groq Whisper
        ↓
2. Image Analysis
   └─→ brain_of_doctor.py
   └─→ Encodes image to base64
   └─→ Sends to LLaMA model with patient query
        ↓
3. AI Response Generation
   └─→ LLaMA model generates doctor response
        ↓
4. Voice Synthesis
   └─→ voice_of_the_doctor.py
   └─→ Converts response to speech via ElevenLabs
        ↓
5. Display Results
   └─→ Show transcription, response, and play audio
```


## 🔑 API Configuration

### Groq API
- Used for: LLaMA vision model and Whisper speech-to-text
- [Get API Key](https://console.groq.com/)
- Rate Limits: Check Groq documentation for current limits

### ElevenLabs API
- Used for: High-quality voice synthesis
- [Get API Key](https://www.elevenlabs.io/)
- Voice ID: `21m00Tcm4TlvDq8ikWAM` (Professional male voice)

## 📝 Limitations

- Requires internet connection for API calls
- Medical analysis is for educational purposes only - not for actual medical diagnosis
- Image analysis limited to formats supported by the API
- Response time depends on API availability and model inference speed
- Audio recording limited to microphone input

## 🎓 Educational Purpose

This project is designed for educational purposes to demonstrate:
- Multimodal AI integration (audio + vision)
- API orchestration and integration
- Speech processing pipelines
- Web UI development with Gradio
- Error handling and user feedback

## 🤝 Contributing

Feel free to extend this project with:
- Additional voice options
- Support for multiple languages
- Medical specialization options
- Session history and context retention
- Advanced image preprocessing

## 📄 License

This project uses third-party APIs and services. Ensure compliance with:
- Groq API Terms of Service
- ElevenLabs API Terms of Service
- Google TTS Terms of Service

## 🔗 Useful Resources

- [Gradio Documentation](https://www.gradio.app/)
- [Groq API Docs](https://console.groq.com/docs/speech-text)
- [ElevenLabs Documentation](https://elevenlabs.io/docs)
- [SpeechRecognition Library](https://github.com/Uberi/speech_recognition)
- [Pydub Documentation](https://github.com/jiaaro/pydub)

## 💡 Future Enhancements

- [ ] Add medical history tracking
- [ ] Support for multiple doctor personas
- [ ] Real-time transcription display
- [ ] Image annotation features
- [ ] Multi-language support
- [ ] Custom medical knowledge base integration
- [ ] Session persistence
- [ ] Advanced diagnostics with confidence scores

👨‍💻 **Athar Ramzan**  
GitHub: [@oathar](https://github.com/oathar)

---