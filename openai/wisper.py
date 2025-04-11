from openai import OpenAI
client = OpenAI()

audio_file= open("audio/trim_sample1.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print(transcription.text)
