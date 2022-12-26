from datetime import datetime, date

import requests

from api.user_management.model import brands
from constants import request_failure_msg, success_msg, record_not_found_msg
from environment_variables import reddit
from sentiment import sentiment_scores


# d = datetime(2022, 11, 24, 9, 30, 0)

def get_mentions(db, keyword, start_date, end_date, sort_by, language, news_api_Key):
    """
    :param keyword:
    :param start_date:
    :param end_date:
    :param sort_by:
    :param language:
    :param news_api_Key:
    :return:
    """
    total_sentiment_positive = 0
    total_sentiment_negative = 0
    total_sentiment_neutral = 0
    mentions_data = []
    mentions_data_dict = []
    mentions_obj = db.query(brands).filter(brands.hashtag == keyword).first()
    if mentions_obj:
        url = "https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy={}&language={}&apiKey={}".format(
            keyword, start_date, end_date, sort_by, language, news_api_Key)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            total_results = data['totalResults']

            articles_data = data['articles']

            for data_obj in articles_data:
                mentions_dict = dict()
                source_dict = dict()
                source_dict['id'] = data_obj['source']['id']
                source_dict['name'] = data_obj['source']['name']
                mentions_dict['source'] = source_dict
                mentions_dict['author'] = data_obj['author']
                mentions_dict['title'] = data_obj['title']
                mentions_dict['description'] = data_obj['description']
                mentions_dict['url'] = data_obj['url']
                mentions_dict['urlToImage'] = data_obj['urlToImage']
                mentions_dict['publishedAt'] = data_obj['publishedAt']
                mentions_dict['content'] = data_obj['content']
                sentiment, total_sentiment_positive, total_sentiment_negative, total_sentiment_neutral = sentiment_scores(
                    sentence=data_obj['description'], total_sentiment_positive=total_sentiment_positive,
                    total_sentiment_negative=total_sentiment_negative, total_sentiment_neutral=total_sentiment_neutral)
                mentions_dict['sentiment'] = sentiment
                mentions_data_dict.append(mentions_dict)
            mentions_data_meta = {
                "total_results": total_results,
                "articles": mentions_data_dict
            }
            db.query(brands).filter(brands.hashtag == keyword).update({
                "news_mentions": mentions_data_meta, "updated_at": datetime.utcnow()
            })
            db.commit()
            news_mentions_obj = db.query(brands).filter(brands.hashtag == keyword).first()
            mentions_data = news_mentions_obj.news_mentions
            message = success_msg
            status_code = 200

        else:
            message = request_failure_msg
            status_code = 400
            mentions_data = []
    else:
        url = "https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy={}&language={}&apiKey={}".format(
            keyword, start_date, end_date, sort_by, language, news_api_Key)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            total_results = data['totalResults']

            articles_data = data['articles']

            for data_obj in articles_data:
                mentions_dict = dict()
                source_dict = dict()
                source_dict['id'] = data_obj['source']['id']
                source_dict['name'] = data_obj['source']['name']
                mentions_dict['source'] = source_dict
                mentions_dict['author'] = data_obj['author']
                mentions_dict['title'] = data_obj['title']
                mentions_dict['description'] = data_obj['description']
                mentions_dict['url'] = data_obj['url']
                mentions_dict['urlToImage'] = data_obj['urlToImage']
                mentions_dict['publishedAt'] = data_obj['publishedAt']
                mentions_dict['content'] = data_obj['content']
                sentiment, total_sentiment_positive, total_sentiment_negative, total_sentiment_neutral = sentiment_scores(
                    sentence=data_obj['description'], total_sentiment_positive=total_sentiment_positive,
                    total_sentiment_negative=total_sentiment_negative, total_sentiment_neutral=total_sentiment_neutral)
                mentions_dict['sentiment'] = sentiment
                mentions_data_dict.append(mentions_dict)
            mentions_data_meta = {
                "total_results": total_results,
                "articles": mentions_data_dict
            }
            db.query(brands).filter(brands.hashtag == keyword).update({
                "news_mentions": mentions_data_meta, "updated_at": datetime.utcnow()
            })
            db.commit()
            news_mentions_obj = db.query(brands).filter(brands.hashtag == keyword).first()
            mentions_data = news_mentions_obj.news_mentions
            message = success_msg
            status_code = 200

        else:
            message = request_failure_msg
            status_code = 400
            mentions_data = []

    return message, status_code, mentions_data


# def get_sentiment_chart_from_newsapi(keyword, start_date, end_date, sort_by, language, news_api_Key):
#     """
#     :param keyword:
#     :param start_date:
#     :param end_date:
#     :param sort_by:
#     :param language:
#     :param news_api_Key:
#     :return:
#     """
#     total_sentiment_positive = 0
#     total_sentiment_negative = 0
#     total_sentiment_neutral = 0
#     sentiment_data = []
#     mentions_data_dict = []
#     url = "https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy={}&language={}&apiKey={}".format(
#         keyword, start_date, end_date, sort_by, language, news_api_Key)
#     response = requests.get(url)
#
#     if response.status_code == 200:
#
#         data = response.json()
#         # print("data", data)
#         total_results = data['totalResults']
#
#         articles_data = data['articles']
#         print("articles_data", articles_data)
#         # 👇️ call strftime() method on datetime object
#         # print(d.strftime('%m/%d/%Y'))  # 👉️ 11/24/2022
#
#         for data_obj in articles_data:
#             sentiment_date_dict = dict()
#             date_format = "%Y-%m-%dT%H:%M:%SZ"
#             published_at = data_obj['publishedAt']
#             published_at = published_at.split('.')
#             published_at_date = datetime.strptime(str(published_at[0]), date_format)
#             print("ajhhhhhhhhhhhhhh", published_at_date.date())
#             if published_at_date == published_at_date:
#                 for date in articles_data:
#                     sentiment, total_sentiment_positive, total_sentiment_negative, total_sentiment_neutral = sentiment_scores(
#                         sentence=date['description'], total_sentiment_positive=total_sentiment_positive,
#                         total_sentiment_negative=total_sentiment_negative,
#                         total_sentiment_neutral=total_sentiment_neutral)
#             date_format = "%Y-%m-%dT%H:%M:%SZ"
#             published_at = date['publishedAt']
#             published_at = published_at.split('.')
#             published_at = datetime.strptime(str(published_at[0]), date_format)
#             sentiment_date_dict['publishedAt'] = published_at.date()
#             sentiment_date_dict['number_of_positive'] = total_sentiment_positive
#             sentiment_date_dict['number_of_negative'] = total_sentiment_negative
#             sentiment_date_dict['number_of_neutral'] = total_sentiment_neutral
#             # importing package
#             # import matplotlib.pyplot as plt
#             # import numpy as np
#             #
#             # # create data
#             # x = sentiment_date_dict['publishedAt']
#             # y = sentiment_date_dict['number_of_positive']
#             #
#             # # plot lines
#             # # plt.plot(x, y, label="line 1")
#             # # plt.plot(y, x, label="line 2")
#             # plt.plot(x, np.sin(x), label="curve 1")
#             # plt.plot(x, np.cos(x), label="curve 2")
#             # plt.legend()
#             # plt.show()
#
#             sentiment_data.append(sentiment_date_dict)
#             # sentiment_data = {
#             #     # "total_results": total_results,
#             #     "publishedAt": published_at,
#             #     "number_of_positive": total_sentiment_positive,
#             #     "number_of_negative": total_sentiment_negative,
#             #     "number_of_neutral": total_sentiment_neutral
#             # }
#         message = success_msg
#         status_code = 200
#
#     else:
#         message = request_failure_msg
#         status_code = 400
#         sentiment_data = []
#
#     return message, status_code, sentiment_data

def get_sentiment_chart_from_newsapi(keyword, start_date, end_date, sort_by, language, news_api_Key):
    """
    :param keyword:
    :param start_date:
    :param end_date:
    :param sort_by:
    :param language:
    :param news_api_Key:
    :return:
    """
    total_sentiment_positive = 0
    total_sentiment_negative = 0
    total_sentiment_neutral = 0
    sentiment_data = []
    url = "https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy={}&language={}&apiKey={}".format(
        keyword, start_date, end_date, sort_by, language, news_api_Key)
    print(url)
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()
        total_results = data['totalResults']
        articles_data = data['articles']

        for data_obj in articles_data:
            sentiment_date_dict = dict()
            sentiment, total_sentiment_positive, total_sentiment_negative, total_sentiment_neutral = sentiment_scores(
                sentence=data_obj['description'], total_sentiment_positive=total_sentiment_positive,
                total_sentiment_negative=total_sentiment_negative,
                total_sentiment_neutral=total_sentiment_neutral)
            date_format = "%Y-%m-%dT%H:%M:%SZ"
            published_at = data_obj['publishedAt']
            published_at = published_at.split('.')
            published_at = datetime.strptime(str(published_at[0]), date_format)
            format_date = published_at.date()
            final_date_format=format_date.strftime('%d/%m/%Y')
            sentiment_date_dict['publishedAt'] = final_date_format
            sentiment_date_dict['number_of_positive'] = total_sentiment_positive
            sentiment_date_dict['number_of_negative'] = total_sentiment_negative
            sentiment_date_dict['number_of_neutral'] = total_sentiment_neutral

            sentiment_data.append(sentiment_date_dict)
        message = success_msg
        status_code = 200

    else:
        message = request_failure_msg
        status_code = 400
        sentiment_data = []

    return message, status_code, sentiment_data


def get_reddit_apis_mentions(db, keyword, limit):
    """
    :param keyword:
    :param limit:
    :return:
    """
    total_sentiment_positive = 0
    total_sentiment_negative = 0
    total_sentiment_neutral = 0
    mentions_data = []
    mentions_obj = db.query(brands).filter(brands.hashtag == keyword).first()
    if mentions_obj:

        response = reddit.subreddit(keyword).hot(limit=limit)
        if response:
            for reddit_obj in response:
                mentions_dict = dict()
                mentions_dict['id'] = reddit_obj.id
                mentions_dict['name'] = reddit_obj.name
                mentions_dict['source'] = 'reddit.com'
                mentions_dict['author'] = str(reddit_obj.author)
                mentions_dict['title'] = reddit_obj.title
                mentions_dict['description'] = reddit_obj.title
                mentions_dict['url'] = reddit_obj.url
                mentions_dict['publishedAt'] = reddit_obj.created_utc
                mentions_dict['score'] = str(reddit_obj.score)
                mentions_dict['selftext'] = str(reddit_obj.selftext)
                mentions_dict['upvote_ratio'] = str(reddit_obj.upvote_ratio)

                sentiment, total_sentiment_positive, total_sentiment_negative, total_sentiment_neutral = sentiment_scores(
                    sentence=reddit_obj.title, total_sentiment_positive=total_sentiment_positive,
                    total_sentiment_negative=total_sentiment_negative, total_sentiment_neutral=total_sentiment_neutral)
                mentions_dict['sentiment'] = sentiment
                mentions_data.append(mentions_dict)
            db.query(brands).filter(brands.hashtag == keyword).update({
                "reddit_mentions": mentions_data, "updated_at": datetime.utcnow()
            })
            db.commit()
        reddit_mentions_obj = db.query(brands).filter(brands.hashtag == keyword).first()
        mentions_data = reddit_mentions_obj.reddit_mentions
        message = success_msg
        status_code = 200
    else:
        response = reddit.subreddit(keyword).hot(limit=limit)
        if response:
            for reddit_obj in response:
                mentions_dict = dict()
                mentions_dict['id'] = reddit_obj.id
                mentions_dict['name'] = reddit_obj.name
                mentions_dict['source'] = 'reddit.com'
                mentions_dict['author'] = str(reddit_obj.author)
                mentions_dict['title'] = reddit_obj.title
                mentions_dict['description'] = reddit_obj.title
                mentions_dict['url'] = reddit_obj.url
                mentions_dict['publishedAt'] = reddit_obj.created_utc
                mentions_dict['score'] = str(reddit_obj.score)
                mentions_dict['selftext'] = str(reddit_obj.selftext)
                mentions_dict['upvote_ratio'] = str(reddit_obj.upvote_ratio)

                sentiment, total_sentiment_positive, total_sentiment_negative, total_sentiment_neutral = sentiment_scores(
                    sentence=reddit_obj.title, total_sentiment_positive=total_sentiment_positive,
                    total_sentiment_negative=total_sentiment_negative, total_sentiment_neutral=total_sentiment_neutral)
                mentions_dict['sentiment'] = sentiment
                mentions_data.append(mentions_dict)
            db.query(brands).filter(brands.hashtag == keyword).update({
                "reddit_mentions": mentions_data, "updated_at": datetime.utcnow()
            })
            db.commit()
            reddit_mentions_obj = db.query(brands).filter(brands.hashtag == keyword).first()
            mentions_data = reddit_mentions_obj.reddit_mentions
            message = success_msg
            status_code = 200
        else:
            mentions_data = []
            message = record_not_found_msg
            status_code = 200

    return message, status_code, mentions_data


def get_sentiment_chart_from_redditapi(keyword, limit):
    """
    :param keyword:
    :param start_date:
    :param limit:
    :return:
    """
    total_sentiment_positive = 0
    total_sentiment_negative = 0
    total_sentiment_neutral = 0
    sentiment_data = []
    response = reddit.subreddit(keyword).hot(limit=limit)
    print(response)
    if response:
        for data_obj in response:
            sentiment_date_dict = dict()
            sentiment, total_sentiment_positive, total_sentiment_negative, total_sentiment_neutral = sentiment_scores(
                sentence=data_obj.title, total_sentiment_positive=total_sentiment_positive,
                total_sentiment_negative=total_sentiment_negative,
                total_sentiment_neutral=total_sentiment_neutral)
            date_format = "%Y-%m-%dT%H:%M:%SZ"
            published_at = data_obj.created_utc
            date_tim = datetime.fromtimestamp(int(published_at)).strftime('%Y-%m-%dT%H:%M:%SZ')
            published_at = date_tim.split('.')
            published_date = datetime.strptime(str(published_at[0]), date_format)
            format_date = published_date.date()
            final_date_format = format_date.strftime('%d/%m/%Y')
            sentiment_date_dict['publishedAt'] = final_date_format
            sentiment_date_dict['number_of_positive'] = total_sentiment_positive
            sentiment_date_dict['number_of_negative'] = total_sentiment_negative
            sentiment_date_dict['number_of_neutral'] = total_sentiment_neutral

            sentiment_data.append(sentiment_date_dict)
        message = success_msg
        status_code = 200

    else:
        message = request_failure_msg
        status_code = 400
        sentiment_data = []

    return message, status_code, sentiment_data
