import logging
import traceback

from api.comparison_management.utils import mentions_comparison_chart
from constants import exception_msg
from environment_variables import news_api_Key


def fetch_mentions_comparison_chart(keyword, start_date, end_date, sort_by, language):
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

        message, status_code, data = mentions_comparison_chart(keyword=keyword, start_date=start_date,
                                                               end_date=end_date, sort_by=sort_by,
                                                               language=language, news_api_Key=news_api_Key)
    except Exception as exc:
        logging.exception(str(exc))
        traceback.print_exc()
        data = []
        message = exception_msg
        status_code = 400
    return message, status_code, data
