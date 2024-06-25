from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

# Инициализация роутера
router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]
)


# Инициализация шаблонов Jinja2
templates = Jinja2Templates(directory="app/templates")


@router.get('/hotels')
async def get_hotels_page(
        request: Request,
        # hotels = Depends()
):
    return templates.TemplateResponse(name="hotels.html", context={'request': request})