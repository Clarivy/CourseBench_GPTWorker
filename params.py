from pydantic import BaseModel

class generateParams(BaseModel):
    title: str
    content: str