from fastapi import FastAPI, HTTPException
from params import generateParams
from generator import Generator

app = FastAPI()
gpt_generator = Generator(config="./examples/config.json")

@app.post("/v1/generate")
async def generate(params: generateParams):
    try:
        messages = gpt_generator.generate(params.content, params.title)
        return messages
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
