from typing import Annotated

from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    text: Annotated[str, Field(min_length=1)]
