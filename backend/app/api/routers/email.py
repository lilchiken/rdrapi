from fastapi import (
    APIRouter,
    status,
)
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import app.db.schemas as schemas
from app.tasks import send_email
from app.core.config import conf

mails = conf.get('name_mails_set')

router_email = APIRouter()


@router_email.post('/subEmail')
def read_email(item: schemas.MailModel):
    try:
        send_email(str(item.email))
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({'detail': 'Thank you for sub!'})
        )
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=jsonable_encoder({'detail': e.__str__()})
        )