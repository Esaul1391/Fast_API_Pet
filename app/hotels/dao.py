from datetime import date

from sqlalchemy import and_, func, insert, or_, select
from sqlalchemy.exc import SQLAlchemyError

from app.hotels.models import Hotels
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.exceptions import RoomFullyBooked
from app.hotels.rooms.models import Rooms
from app.logger import logger


class HotelsDAO(BaseDAO):
    model = Hotels

    @staticmethod
    async def search_for_hotels(location: str, date_from: date, date_to: date):
        async with async_session_maker() as session:
            query = (
                select(Hotels)
                .join(Rooms, Hotels.id == Rooms.hotel_id)
                .where(
                    and_(
                        Hotels.location == location,
                        Rooms.available_from <= date_from,
                        Rooms.available_to >= date_to
                    )
                )
                .group_by(Hotels.id)
            )
            result = await session.execute(query)
            return result.scalars().all()