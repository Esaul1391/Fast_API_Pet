from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel

app = FastAPI()  # вызываю класс fastapi


class SHotel(BaseModel):
    address: str
    name: str
    stars: int



@app.get('/hotels', response_model=list[SHotel])
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: bool = Query(default=None),
    stars: int = Query(ge=1, le=5, default=None)  # >= 1 и <= 5
    ):
    hotels = [
        {
            "address": 'Какойто адрес',
            "name": 'Super Hotel',
            "stars": 5
        }
    ]
    return hotels


class SBooking(BaseModel):  # поля для POST запроса
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass