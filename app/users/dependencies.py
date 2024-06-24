from datetime import datetime

from fastapi import Request, HTTPException, Depends, status
from jose import JWTError, jwt  # Используйте jose для работы с JWT

from app.exceptions import IncorrectEmailOrPasswordException, TokenAbsentException, TokenExpiredException, \
    UserIsNotPresentException
from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        # Используйте jwt.decode() для декодирования токена
        payload = jwt.decode(
            token, 'asdajasasASDASD', algorithms=['HS256']
        )
    except JWTError:
        raise TokenAbsentException

    expire: int = payload.get("exp")
    if (not expire) or (datetime.fromtimestamp(expire) < datetime.utcnow()):
        raise IncorrectEmailOrPasswordException

    user_id: str = payload.get('sub')
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersDAO.find_by_id(int(user_id))
    # user = UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user

