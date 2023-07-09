"""
This is a FastAPI application that uses a GPT generator to generate messages based on the provided content and title.
The application exposes a POST endpoint at /v1/generate which accepts parameters for content and title.
In case of any exceptions during the generation of messages, a HTTPException with status code 500 is returned.
"""

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
