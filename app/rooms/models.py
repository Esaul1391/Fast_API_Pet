from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed
from app.database import Base


# понять зачем я наследуюсь от Base?
class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey("hotels.id"))
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    services = Column(JSON)
    quantity = Column(Integer)
    image_id = Column(Integer)