import requests
from constants import success_msg, request_failure_msg
from datetime import datetime


def mentions_comparison_chart(keyword, start_date, end_date, sort_by, language, news_api_Key):
    """
    :param keyword:
    :param start_date:
    :param end_date:
    :param sort_by:
    :param language:
    :param news_api_Key:
    :return:
    """
    number_of_mentions = 0
    sentiment_data = []
    url = "https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy={}&language={}&apiKey={}".format(
        keyword, start_date, end_date, sort_by, language, news_api_Key)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        total_results = data['totalResults']

        articles_data = data['articles']
        for data_obj in articles_data:
            sentiment_date_dict = dict()
            date_format = "%Y-%m-%dT%H:%M:%SZ"
            published_at = data_obj['publishedAt']
            published_at = published_at.split('.')
            published_at = datetime.strptime(str(published_at[0]), date_format)
            format_date = published_at.date()
            final_date_format = format_date.strftime('%d/%m/%Y')
            # if final_date_format == final_date_format:
            #     for data in articles_data:
            #         number_of_mentions = data.count()


            date_format = "%Y-%m-%dT%H:%M:%SZ"
            published_at = data_obj['publishedAt']
            published_at = published_at.split('.')
            published_at = datetime.strptime(str(published_at[0]), date_format)
            format_date = published_at.date()
            final_date_format = format_date.strftime('%d/%m/%Y')
            sentiment_date_dict['publishedAt'] = final_date_format
            sentiment_date_dict['number_of_mentions'] = number_of_mentions
            sentiment_data.append(sentiment_date_dict)
        message = success_msg
        status_code = 200
        # published_at = start_date
        #
        # mentions_data = {
        #     "total_results": total_results,
        #     "published_at": published_at
        # }
        # message = success_msg
        # status_code = 200

    else:
        message = request_failure_msg
        status_code = 400
        sentiment_data = []

    return message, status_code, sentiment_data
