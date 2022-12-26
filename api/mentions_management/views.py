import logging
import traceback

from api.mentions_management.utils import get_mentions, get_sentiment_chart_from_newsapi, get_reddit_apis_mentions, \
    get_sentiment_chart_from_redditapi
from constants import exception_msg
from environment_variables import news_api_Key


def fetch_mentions_from_newsapi(db, keyword, start_date, end_date, sort_by, language):
    print(keyword,start_date,end_date,sort_by,language)
    """
    :param db:
    :param keyword:
    :param start_date:
    :param end_date:
    :param sort_by:
    :param language:
    :return:
    """
    try:

        message, status_code, data = get_mentions(db=db, keyword=keyword, start_date=start_date,
                                                  end_date=end_date, sort_by=sort_by,
                                                  language=language, news_api_Key=news_api_Key)
    except Exception as exc:
        logging.exception(str(exc))
        traceback.print_exc()
        data = []
        message = exception_msg
        status_code = 400
    return message, status_code, data


def fetch_sentiment_chart(keyword, start_date, end_date, sort_by, language):
    """
    :param db:
    :param keyword:
    :param start_date:
    :param end_date:
    :param sort_by:
    :param language:
    :return:
    """
    try:

        message, status_code, data = get_sentiment_chart_from_newsapi(keyword=keyword, start_date=start_date,
                                                                      end_date=end_date, sort_by=sort_by,
                                                                      language=language, news_api_Key=news_api_Key)
    except Exception as exc:
        logging.exception(str(exc))
        traceback.print_exc()
        data = []
        message = exception_msg
        status_code = 400
    return message, status_code, data


def fetch_mentions_from_reddit_apis(db, keyword, limit):
    """
    :param db:
    :param keyword:
    :param limit:
    :return:
    """
    try:

        message, status_code, data = get_reddit_apis_mentions(db=db, keyword=keyword, limit=limit)
    except Exception as exc:
        logging.exception(str(exc))
        traceback.print_exc()
        data = []
        message = exception_msg
        status_code = 400
    return message, status_code, data


def fetch_reddit_sentiment_chart(keyword, limit):
    """
    :param db:
    :param keyword:
    :param limit:
    :return:
    """
    try:

        message, status_code, data = get_sentiment_chart_from_redditapi(keyword=keyword, limit=limit)
    except Exception as exc:
        logging.exception(str(exc))
        traceback.print_exc()
        data = []
        message = exception_msg
        status_code = 400
    return message, status_code, data