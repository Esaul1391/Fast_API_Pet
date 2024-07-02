from datetime import date
from typing import List
from app.users.models import Users
from app.users.dependencies import get_current_user
from fastapi import APIRouter, Request, Depends
from fastapi_versioning import version



from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
# from app.bookings.service import BookingService
from app.exceptions import RoomCannotBeBooked

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get('')
@version(1)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)

# @router.post("", status_code=201)
# async def add_booking(
#
#     booking: SNewBooking,
#     background_tasks: BackgroundTasks,
#     user: Users = Depends(get_current_user),
# ):
#     new_booking = await BookingService.add_booking(
#         booking,
#         background_tasks,
#         user
#     )
#     return new_booking

@router.post('')
@version(1)
async def add_booking(
        room_id: int, date_from: date, date_to: date,
        user: Users = Depends(get_current_user),
    ):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked

# @router.get("",  response_model=List[SBooking])
# async def get_bookings() -> List[SBooking]:
#     return await BookingDAO.find_all()

    # async with async_session_maker() as session:
    #     query = select(Bookings)  # SELECT * FROM bookings;
    #     result = await session.execute(query)
    #     return result.scalars().all()