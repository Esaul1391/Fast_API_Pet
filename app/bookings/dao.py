# Data Access Object работаю с базой данных
from app.database import async_session_maker
from sqlalchemy import select
from app.bookings.models import Bookings
from app.dao.base import BaseDAO

class BookingDAO(BaseDAO):
    model = Bookings

