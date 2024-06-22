from typing import List
from app.users.models import Users
from app.users.dependencies import get_current_user
from fastapi import APIRouter, Request, Depends
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=user.id)

# @router.get("",  response_model=List[SBooking])
# async def get_bookings() -> List[SBooking]:
#     return await BookingDAO.find_all()

    # async with async_session_maker() as session:
    #     query = select(Bookings)  # SELECT * FROM bookings;
    #     result = await session.execute(query)
    #     return result.scalars().all()

