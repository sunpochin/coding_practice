from typing import List

from pydantic import BaseModel


class Author(BaseModel):
    name: str
    books: List[str]

