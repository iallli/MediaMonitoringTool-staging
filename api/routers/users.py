from typing import Optional

import humps
from fastapi import APIRouter, Response, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from api.user_management.user_schema import usersSchema, CreateBrandSchema
from api.user_management.views import add_company_user, company_user_login, add_brand, fetch_brands_listing
from constants import response_body
from models import get_db

router = APIRouter()


@router.post('/api/v1/users/signup', tags=['User Management'])
def user_signup(response: Response, user_schema: usersSchema, db: Session = Depends(get_db)):
    message, status_code = add_company_user(db=db, email=user_schema.email, password=user_schema.password)

    response_body['message'] = message
    response_body['data'] = []
    response.status_code = status_code

    return JSONResponse(content=response_body, status_code=response.status_code)


@router.post('/api/v1/users/login', tags=['User Management'])
def user_login(response: Response, user_schema: usersSchema, db: Session = Depends(get_db)):
    message, status_code, user_data = company_user_login(db=db, email=user_schema.email,
                                                         password=user_schema.password)

    response_body['message'] = message
    response_body['data'] = humps.camelize(user_data)
    response.status_code = 200

    return JSONResponse(content=response_body, status_code=response.status_code)


@router.post('/api/v1/users/create-brand', tags=['User Management'])
def create_brand(response: Response, create_brand_schema: CreateBrandSchema, db: Session = Depends(get_db)):
    message, status_code = add_brand(db=db,
                                     brand_competitor_hashtag_keywords=create_brand_schema.enter_brand_competitor_hashtag,
                                     email=create_brand_schema.email)

    response_body['message'] = message
    response_body['data'] = []
    response.status_code = status_code

    return JSONResponse(content=response_body, status_code=response.status_code)


@router.post('/api/v1/users/brands_listing', tags=['User Management'])
def get_brands_listing(response: Response, accountType: Optional[str] = 'trial', email: Optional[str] = None,
                       db: Session = Depends(get_db)):
    message, status_code, data = fetch_brands_listing(db=db, account_type=accountType, email=email)

    response_body['message'] = message
    response_body['data'] = humps.camelize(jsonable_encoder(data))
    response.status_code = status_code

    return JSONResponse(content=response_body, status_code=response.status_code)
