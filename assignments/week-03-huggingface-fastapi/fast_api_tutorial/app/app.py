from fastapi import FastAPI
from pydantic import BaseModel 
from transformers import pipeline

class TextToTranslate(BaseModel):
    input_text: str


class TextsToTranslate (BaseModel): 
    input_texts: list 

translator_pipeline = pipeline("translation_en_to_fr", model = '/home/tfarotimi/Fourth Brain Projects/Tope-Farotimi-MLE/assignments/week-03-huggingface-fastapi/fast_api_tutorial/app/model/En_to_Fr')

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

@app.post("/translate")
def translate(text_to_translate: TextToTranslate):
    return {"translation": translator_pipeline(text_to_translate.input_text)}

@app.post("/batch_translate")
def batch_translate(texts_to_translate: TextsToTranslate):
    results = []
    for i in texts_to_translate.input_texts:
        results.append(translator_pipeline(i))

    return {"translations":results}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)