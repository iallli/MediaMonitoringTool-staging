# from pprint import pprint
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import praw
#
# user_agent = "Ali 1.0 by /user/iallli"
# reddit = praw.Reddit(
#     client_id='JnvZiIF4j4Du62s36w_rjg',
#     client_secret='0mPVZ3tcb2vbqCu94TEfw4byJieREw',
#     user_agent=user_agent
# )
# import datetime
#
# headlines = set()
# for submission in reddit.subreddit('apple').top("all"):
#
#     if (submission.selftext == ''):
#         submission.selftext = 'This user did not comment on this.'
#
#     #     print('Author Name: '+str(submission.author))
#     #     print('Submission Title: '+submission.title)
#     #     print('Comment: '+submission.selftext)
#     #     print('Created Date: '+str(datetime.datetime.utcfromtimestamp(submission.created_utc)))
#     #     print('Score: '+str(submission.score))
#     #     print("\n")
#
#     headlines.add(submission.title)
#     # headlines.add(submission.selftext)
#
# # print(len(headlines))
# print(headlines)
# df = pd.DataFrame(headlines)
# print(df)
# df.columns = ['Headline']
# print(df)
# df.to_csv('headlines.csv', header=False, encoding='utf-8', index=False)
# df
# import nltk
#
# nltk.download('vader_lexicon')
# from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
#
# sia = SIA()
# import csv
# result = []
# from textblob import TextBlob
#
# infile = 'headlines.csv'
#
# with open(infile, encoding="utf8") as csvfile:
#     rows = csv.reader(csvfile)
#     for row in rows:
#         sentence = row[0]
#         blob = TextBlob(sentence)
#         print(blob.sentiment)
#
# for line in headlines:
#     pol_score = TextBlob(line)
#     pol_score['headlines'] = pol_score.sentimentline
#     result.append(pol_score)
#
# pprint(result[:5], width=100)
# df = pd.DataFrame.from_records(result)
# df.head()
# df['label'] = 0
# df.loc[df['compound'] > 0.2, 'label'] = 1
# df.loc[df['compound'] < -0.2, 'label'] = -1
# df.head()
# df2 = df[['headlines', 'label']]
# df2.to_csv('reddit_headlines_label.csv', encoding='utf-8', index=False)
# df.label.value_counts()
# df.label.value_counts(normalize=True) * 100
# print("Positive Headlines:\n")
# pprint(list(df[df['label'] == 1].headlines)[:5], width=1000)
#
# print("\nNegative Headlines:\n")
# pprint(list(df[df['label'] == -1].headlines)[:5], width=1000)
# fig, ax = plt.subplots(figsize=(8, 8))
# counts = df.label.value_counts(normalize=True) * 100
# sns.barplot(x=counts.index, y=counts, ax=ax)
# ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
# ax.set_ylabel("Percentage")
# plt.show()
#
#


# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#
#
# def sentiment_scores(sentence, total_sentiment_positive=None, total_sentiment_negative=None, total_sentiment_neutral=None):
#
#     sid_obj = SentimentIntensityAnalyzer()
#
#     sentiment_dict = sid_obj.polarity_scores(sentence)
#
#     print("Overall sentiment dictionary is : ", sentiment_dict)
#     print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
#     print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
#     print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")
#
#     print("Sentence Overall Rated As", end=" ")
#
#     # decide sentiment as positive, negative and neutral
#     if sentiment_dict['compound'] >= 0.05:
#         # print("Positive")
#         sentiment = "Positive"
#         total_sentiment_positive = total_sentiment_positive + 1
#         # print("total_sentiment_positive", total_sentiment_positive)
#
#     elif sentiment_dict['compound'] <= - 0.05:
#         # print("Negative")
#         sentiment = "Negative"
#         total_sentiment_negative = total_sentiment_negative + 1
#         # print("total_sentiment_negative", total_sentiment_negative)
#     else:
#         # print("Neutral")
#         sentiment = "Neutral"
#         total_sentiment_neutral = total_sentiment_neutral + 1
#         # print("total_sentiment_neutral", total_sentiment_neutral)
#
#     return sentiment, total_sentiment_positive, total_sentiment_negative, total_sentiment_neutral


from textblob import TextBlob


def comparison_sentiment_scores(sentence, number_of_mentions=None):
    compound = 0
    blob = TextBlob(str(sentence))
    blob.sentiment
    compound = blob.sentiment.polarity
    # decide sentiment as positive, negative and neutral
    # if compound > 0:
    #     sentiment = "Positive"
    #     total_sentiment_positive = total_sentiment_positive + compound
    #
    # elif compound < 0:
    #     sentiment = "Negative"
    #     total_sentiment_negative = total_sentiment_negative + compound
    # else:
    #     sentiment = "Neutral"
    #     total_sentiment_neutral = total_sentiment_neutral + compound

    return sentiment, total_sentiment_positive, total_sentiment_negative, total_sentiment_neutral



def sentiment_scores(sentence, total_sentiment_positive=None, total_sentiment_negative=None,
                     total_sentiment_neutral=None):
    compound = 0
    blob = TextBlob(str(sentence))
    blob.sentiment
    compound = blob.sentiment.polarity
    # decide sentiment as positive, negative and neutral
    if compound > 0:
        sentiment = "Positive"
        total_sentiment_positive = total_sentiment_positive + compound

    elif compound < 0:
        sentiment = "Negative"
        total_sentiment_negative = total_sentiment_negative + compound
    else:
        sentiment = "Neutral"
        total_sentiment_neutral = total_sentiment_neutral + compound

    return sentiment, total_sentiment_positive, total_sentiment_negative, total_sentiment_neutral
