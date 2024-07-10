from datetime import timedelta

from typing import Annotated

from fastapi import APIRouter


router = APIRouter(
    prefix="/api/locations",
    tags=["auth"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post("/")
async def get_locations():
    return "Hello"
