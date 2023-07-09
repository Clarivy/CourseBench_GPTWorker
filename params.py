"""
This file contains the class definition for `generateParams`. 
`generateParams` is a Pydantic BaseModel that is used to validate the data 
that is passed to it. It has two fields: `title` and `content`, both of which 
are required and must be of type `str`.
"""

from pydantic import BaseModel

class generateParams(BaseModel):
    title: str
    content: str