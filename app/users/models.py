from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed
from app.database import Base


# понять зачем я наследуюсь от Base?
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
