from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI()
translator = Translator()

class TranslationRequest(BaseModel):
    text: str
    dest: str

@app.post("/translate")
def translate_text(request: TranslationRequest):
    result = translator.translate(request.text, dest=request.dest)
    return {"translated_text": result.text, "src": result.src, "dest": result.dest}
