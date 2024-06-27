# from datetime import date, datetime
# from pydantic import parse_obj_as
# from fastapi import APIRouter, Query
# from app.hotels.dao import HotelsDAO
#
# from fastapi_cache.decorator import cache
# import asyncio
#
# router = APIRouter(prefix="/hotels", tags=["Отели"])
#
#
# @router.get("/{location}")
# @cache(expire=30)
# async def get_hotels_by_location_and_time(
#         location: str,
#         date_from: date = Query(..., description=f'пример, {datetime.now().date()}'),
#         date_to: date = Query(..., description=f'пример, {datetime.now().date()}'),
# ):
#     # await asyncio.sleep(3)
#     hotels = await HotelsDAO.search_for_hotels(location, date_from, date_to)
#     hotels_json = parse_obj_as(List[HotelInfo], hotels)         # вернет объект json а не SQL требуется для redis
#     return hotels_json