from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/api/locations",
    tags=["auth"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.get("/", response_class=HTMLResponse)
async def get_locations():
    coordinates = [
        {"lat": "18.9750", "lng": "72.8258"},
        {"lat": "19.0760", "lng": "72.8777"},
        {"lat": "19.2183", "lng": "72.9781"}
    ]

    with open('server/static/google map.html', 'r') as file:
        html_content = file.read()

    coordinates_js = ', '.join([f'{{lat: "{coord["lat"]}", lng: "{coord["lng"]}"}}' for coord in coordinates])

    html_content = html_content.replace('__COORDINATES__', coordinates_js)

    return html_content
