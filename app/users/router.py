from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.users.auth import get_password_hash, authenticate_user, crate_access_token
from app.users.dependencies import get_current_user
from app.users.schemas import SUserAuth
from app.users.dao import UsersDAO

router = APIRouter(
    prefix='/auth',
    tags=['Auth & Пользователи']
)


# не забывать импортировать в main
@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    #   если пользователь есть возвращаю ошибку
    if existing_user:
        raise UserAlreadyExistsException
    #   если нет хеширую данные и добавляю пользователя в БД
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


#   создаю endpoint для авторизации пользователя
@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = crate_access_token({'sub': str(user.id)})
    #   оставляю куки в браузере пользователя
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('booking_access_token')


@router.get('/me')
async def read_users_me(current_user: str = Depends(get_current_user)):
    return current_user
