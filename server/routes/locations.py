from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/api/locations",
    tags=["auth"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.get("/", response_class=HTMLResponse)
async def get_locations():
    with open('server/static/google map.html', 'r') as file:
        html_content = file.read()
    return html_content
