from typing import Annotated, Any

from fastapi import APIRouter, Depends, File, UploadFile

from .auth import verify_key
from .schemas import AnalyzeResult
from .service import process_receipt_upload, process_receipt_url

router = APIRouter()

# TODO: Remove this
AuthKey = Annotated[str, Depends(verify_key)]


@router.post("/url_receipt/", response_model=AnalyzeResult)
async def url_receipt(key: AuthKey, image_url: str) -> dict[str, Any]:
    """Process the URL of a receipt image and return the classified data."""
    return await process_receipt_url(image_url=image_url)


@router.post("/upload_receipt/", response_model=AnalyzeResult)
async def upload_receipt(key: AuthKey, file: UploadFile = File(...)) -> dict[str, Any]:
    """Process a receipt image and return the classified data."""
    return await process_receipt_upload(file=file)
