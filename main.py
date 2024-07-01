from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, EmailStr, conint, constr
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder

app = FastAPI()


class User(BaseModel):
    username: str
    age: conint(gt=18)
    email: EmailStr
    password: constr(min_length=8, max_length=16)
    phone: Optional[str] = 'Unknown'


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Извлечение детальной информации об ошибках валидации
    errors = exc.errors()
    details = []
    for error in errors:
        loc = " -> ".join(error['loc'])
        msg = error['msg']
        details.append(f"{loc}: {msg}")

    return JSONResponse(
        status_code=422,
        content={"detail": "Ошибка проверки данных", "errors": details}
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder({"detail": exc.detail})
    )


@app.post("/user/")
async def create_user(user: User):
    if user.username in user.password:
        raise HTTPException(status_code=400, detail="Пароль не должен содержать имя пользователя.")
    return {"message": "Пользователь создан", "user": user.model_dump()}
