import torch
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

model_path = "/app/model_weights"


class InputData(BaseModel):
    text: str
    target_lang: str


def translate_nllb(model_name, input_text, target_lang_code, max_length=250):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = model.to(device)
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
    inputs = {key: value.to(device) for key, value in inputs.items()}
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang_code)
    translated_tokens = model.generate(
        **inputs, forced_bos_token_id=forced_bos_token_id, max_length=max_length
    )
    output = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    return output


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/translate")
async def translate(request: Request, text: str = Form(...), target_lang: str = Form(...)):
    translation = translate_nllb(model_path, text, target_lang)
    return templates.TemplateResponse("index.html", {"request": request, "translation": translation, "original": text})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
