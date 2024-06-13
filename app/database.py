from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

# Генерирую URL базы данных
# asyncpg выполняет запросы к базе асинхронно
# Асинхронные запросы к базе данных позволяют во время ожидания ответа от БД обрабатывать другие запросы
# DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# передаю в алхимию URL
engine = create_async_engine(settings.DATABASE_URL)

# создаю генератор сессий, это транзакции к базе данных
# транзакция это набор инструкций которы мы посылаем в базу данных
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# класс Base используется для миграций, все модели мы будем аккумулировать данные о миграциях,
# будет передаваться в alembic
class Base(DeclarativeBase):
    pass
