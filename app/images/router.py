from fastapi import UploadFile, APIRouter
import shutil  # библиотека для сохранения картинки

from app.tasks.tasks import process_pic

router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"]
)


@router.post('/hotels')  # создал роутер для загрузки изображений
async def add_hotel_image(name: int, file: UploadFile):
    im_path = f"app/static/images{name}.webp"  # не предавать классом path
    with open(im_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(im_path)
