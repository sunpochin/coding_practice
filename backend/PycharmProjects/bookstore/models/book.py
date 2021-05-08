from pydantic import BaseModel, Field
from models.author import Author
from utils.const import ISBN_SUMMARY, ISBN_DESCRIPTION


class Book(BaseModel):
    isbn: str = Field(None, description=ISBN_DESCRIPTION)
    name: str
    author: Author
    year: int = Field(None, lt=1900, gt=2100)

