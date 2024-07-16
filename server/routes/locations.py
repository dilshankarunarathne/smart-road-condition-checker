from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse

from server.services.query import query_all_locations

router = APIRouter(
    prefix="/api/locations",
    tags=["auth"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.get("/", response_class=HTMLResponse)
async def get_locations():
    coordinates = query_all_locations()

    with open('server/static/google map.html', 'r') as file:
        html_content = file.read()

    # Replace __COORDINATES__ with the actual coordinates

    html_content = html_content.replace('__COORDINATES__', coordinates_js)

    return html_content
