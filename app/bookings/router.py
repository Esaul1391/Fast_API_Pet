from fastapi import APIRouter
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_bookings() -> SBooking:
    return await BookingDAO.find_all()

    # async with async_session_maker() as session:
    #     query = select(Bookings)  # SELECT * FROM bookings;
    #     result = await session.execute(query)
    #     return result.scalars().all()

