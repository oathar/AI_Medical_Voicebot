#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi, this is a test of text to speech conversion using gTTS and ElevenLabs."
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text= input_text,
        voice_id= "21m00Tcm4TlvDq8ikWAM",
        output_format= "mp3_22050_32",
        model_id= "eleven_turbo_v2_5"
    )
    elevenlabs.save(audio, output_filepath)

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing.mp3")
