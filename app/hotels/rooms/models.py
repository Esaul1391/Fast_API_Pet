from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed
from sqlalchemy.orm import Mapped, mapped_column


from app.database import Base


# понять зачем я наследуюсь от Base?
class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    services: Mapped[list[str]] = mapped_column(JSON)
    # services: Mapped[Optional[list[str]]] = mapped_column(JSON)
    quantity: Mapped[int]
    image_id: Mapped[int]


# class Rooms(Base):
#     __tablename__ = "rooms"
#
#     id = Column(Integer, primary_key=True)
#     hotel_id = Column(ForeignKey("hotels.id"))
#     name = Column(String)
#     description = Column(String)
#     price = Column(Integer)
#     services = Column(JSON)
#     quantity = Column(Integer)
#     image_id = Column(Integer)