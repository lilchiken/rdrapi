from fastapi import (
    FastAPI,
    status
)
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
import uvicorn

from app.api.routers import (
    email,
    rdr
)
from app.db.session import SessionLocal


app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000/",
    "http://localhost:8080/",
    "http://localhost",
    "http://localhost:8000/",
    "http://localhost:8888/",
    "http://localhost:5432/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rdr.router_rdr, prefix='/api', tags=['rdr'])
app.include_router(email.router_email, prefix='/api', tags=['email'])


@app.exception_handler(ValidationError)
def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True, port=8888)
