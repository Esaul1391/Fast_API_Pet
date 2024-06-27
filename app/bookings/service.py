


# class BookingService:
#     @classmethod    # не требуется создавать экземпляр класса
#     async def add_booking(cls,
#             booking: SNewBooking,
#             background_tasks: BackgroundTasks,
#             user: Users,
#     ):
#         booking = await BookingDAO.add(
#             user.id,
#             booking.room_id,
#             booking.date_from,
#             booking.date_to,
#         )
#         if not booking:
#             raise RoomCannotBeBooked
#         # TypeAdapter и model_dump - это новинки версии Pydantic 2.0
#         booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
#         # Celery - отдельная библиотека
#         # send_booking_confirmation_email.delay(booking, user.email)
#         # Background Tasks - встроено в FastAPI
#         # background_tasks.add_task(send_booking_confirmation_email, booking, user.email)
#         return booking