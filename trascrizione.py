import whisper

model = whisper.load_model("medium")

result = model.transcribe("Fondamenti_27_03_pt1.mp4", language="it")

with open("trascrizione.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
