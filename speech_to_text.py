import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
with sr.AudioFile("audio.wav") as source:
    audio_data = recognizer.record(source)

# Convert speech to text
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcription:")
    print(text)

except sr.UnknownValueError:
    print("Sorry, could not understand the audio")

except sr.RequestError as e:
    print(f"API error: {e}")
