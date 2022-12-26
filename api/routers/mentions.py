from typing import Optional

import humps
from fastapi import APIRouter, Response, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from api.mentions_management.views import fetch_mentions_from_newsapi, fetch_sentiment_chart, \
    fetch_mentions_from_reddit_apis, fetch_reddit_sentiment_chart
from constants import response_body
from models import get_db

router = APIRouter()


@router.get('/api/v1/mentions/mentions', tags=['Mentions'])
def get_mentions_from_newsapi(response: Response, keyword: str, startDate: Optional[str] = None,
                              endDate: Optional[str] = None, sortBy: Optional[str] = None,
                              language: Optional[str] = None, db: Session = Depends(get_db)):
    message, status_code, data = fetch_mentions_from_newsapi(db=db, keyword=keyword, start_date=startDate,
                                                             end_date=endDate,
                                                             sort_by=sortBy, language=language)

    response_body['message'] = message
    response_body['data'] = humps.camelize(jsonable_encoder(data))
    response.status_code = status_code

    return JSONResponse(content=response_body, status_code=response.status_code)


@router.get('/api/v1/mentions/show-sentiment-chart', tags=['Mentions'])
def show_sentiment_chart(response: Response, keyword: str, startDate: Optional[str] = None,
                         endDate: Optional[str] = None, sortBy: Optional[str] = None,
                         language: Optional[str] = None):
    message, status_code, data = fetch_sentiment_chart(keyword=keyword, start_date=startDate,
                                                       end_date=endDate,
                                                       sort_by=sortBy, language=language)

    response_body['message'] = message
    response_body['data'] = humps.camelize(jsonable_encoder(data))
    response.status_code = status_code

    return JSONResponse(content=response_body, status_code=response.status_code)


@router.get('/api/v1/reddit/mentions/mentions', tags=['Mentions'])
def get_mentions_from_reddit_apis(response: Response, keyword: str, limit: Optional[int] = 10,
                                  db: Session = Depends(get_db)):
    message, status_code, data = fetch_mentions_from_reddit_apis(db=db, keyword=keyword, limit=limit)

    response_body['message'] = message
    response_body['data'] = humps.camelize(jsonable_encoder(data))
    response.status_code = status_code

    return JSONResponse(content=response_body, status_code=response.status_code)


@router.get('/api/v1/mentions/show-reddit-sentiment-chart', tags=['Mentions'])
def show_reddit_sentiment_chart(response: Response, keyword: str, limit: Optional[int] = 100):
    message, status_code, data = fetch_reddit_sentiment_chart(keyword=keyword, limit=limit)

    response_body['message'] = message
    response_body['data'] = humps.camelize(jsonable_encoder(data))
    response.status_code = status_code

    return JSONResponse(content=response_body, status_code=response.status_code)
