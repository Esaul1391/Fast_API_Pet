from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed
from sqlalchemy.orm import relationship

from app.database import Base


# понять зачем я наследуюсь от Base?
# Модель написана в соответствии со старым стилем Алхимии (версии 1.x)
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    booking = relationship("Bookings", back_populates="user")

    def __str__(self):
        return f"Пользователь {self.email}"


# class Users(Base):
#     bookings = None
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True)
#     email = Column(String)
#     hashed_password = Column(String)
#
#     booking = relationship('Bookings', back_populates='user')
#
#     def __str__(self):
#         return f'User {self.email}'
