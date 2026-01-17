#Step1: Setup Audio recorder (ffmpeg & portaudio)
# ffmpeg, portaudio, pyaudio
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as a WAV file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_limit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to a WAV file (no ffmpeg needed)
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="wav")
            
            logging.info(f"Audio saved to {file_path}")
            
            # Transcribe the audio
            try:
                text = recognizer.recognize_google(audio_data)
                logging.info(f"Transcription: {text}")
                return text
            except sr.UnknownValueError:
                logging.error("Could not understand the audio")
                return None
            except sr.RequestError as e:
                logging.error(f"Could not request results from Google Speech Recognition service; {e}")
                return None

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

# Test code moved to if __name__ == "__main__" block

#Step2: Setup Speech to text–STT–model for transcription
import os
from groq import Groq

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
stt_model="whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)
    
    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )

    return transcription.text

if __name__ == "__main__":
    audio_filepath="patient_voice_test_for_patient.wav"
    transcription = record_audio(file_path=audio_filepath)
    if transcription:
        print(f"Patient's voice transcription: {transcription}")
    else:
        print("No transcription available.")