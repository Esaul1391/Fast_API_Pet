import json
import asyncio
import pytest
from app.database import Base, async_session_maker, engine
from app.config import settings
from datetime import datetime
from sqlalchemy import insert

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.users.models import Users

from fastapi.testclient import  TestClient  #   импортируется из httpx
from httpx import AsyncClient, ASGITransport
from app.main import app as fastapi_app


@pytest.fixture(scope='session', autouse=True)  # фикстура это функция которая подготавливает определенную среду для тестирования
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)  # create all table

    def open_mock_json(model: str):
        with open(f'app/tests/mock_{model}.json', 'r') as file:
            return json.load(file)

    hotels = open_mock_json("hotels")
    rooms = open_mock_json("rooms")
    users = open_mock_json("users")
    bookings = open_mock_json("bookings")

    for booking in bookings:
        booking["date_from"] = datetime.strptime(booking["date_from"], "%Y-%m-%d")
        booking["date_to"] = datetime.strptime(booking["date_to"], "%Y-%m-%d")

    async with async_session_maker() as session:    # вставляем данные в алхимию
        for Model, values in [
            (Hotels, hotels),
            (Rooms, rooms),
            (Users, users),
            (Bookings, bookings),
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()


# Взято из документации к pytest-asyncio
@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='function')
async def ac():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url="http://test") as ac:
        yield ac

@pytest.fixture(scope='session')
async def authenticated_ac():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url="http://test") as ac:
        await ac.post('auth/login', json={
            'email': 'test@test.com',
            'password': 'test',
        })
        assert ac.cookies["booking_access_token"]
        yield ac

@pytest.fixture(scope='function')
async def session():
    async with async_session_maker() as session:
        yield session
