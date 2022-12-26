from typing import Optional

import humps
from fastapi import APIRouter, Response, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from api.comparison_management.views import fetch_mentions_comparison_chart
from constants import response_body
from models import get_db

router = APIRouter()


@router.get('/api/v1/comparison/mentions', tags=['Comparison'])
def get_mentions_comparison_chart(response: Response, keyword: str, startDate: Optional[str] = None,
                                  endDate: Optional[str] = None, sortBy: Optional[str] = None,
                                  language: Optional[str] = None):
    message, status_code, data = fetch_mentions_comparison_chart(keyword=keyword, start_date=startDate,
                                                                 end_date=endDate,
                                                                 sort_by=sortBy, language=language)

    response_body['message'] = message
    response_body['data'] = humps.camelize(jsonable_encoder(data))
    response.status_code = status_code

    return JSONResponse(content=response_body, status_code=response.status_code)
