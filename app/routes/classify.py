from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic_models.classify import TextRequest
from services.classify_service import ClassificationService

router = APIRouter()


@router.post("/classify")
async def classify_text(
    text_request: TextRequest,
    classification_service: Annotated[ClassificationService, Depends()],
):
    text = text_request.text

    return classification_service.classify_text(text)
