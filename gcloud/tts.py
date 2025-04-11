from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(
    text="それでは授業を始めていきましょう。 今回も新しい文章を読んでいこうと思います。 手元に青ペンを準備して、話を聞いてみてください。 物語文の大事なポイントは、その人の心情を追いかけることだけど、 心情と同時に、"
)

voice = texttospeech.VoiceSelectionParams(
    language_code="ja-JP",
    name="ja-JP-Chirp3-HD-Aoede"
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

# バイナリとして.wavファイルに保存
with open("output.wav", "wb") as out:
    out.write(response.audio_content)

print("WAVファイル 'output.wav' に保存しました")
