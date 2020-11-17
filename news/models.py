from django.db import models
from HyperNews_Portal.settings import NEWS_JSON_PATH
import json


def get_news_articles():
    with open(NEWS_JSON_PATH, "r") as json_file:
        return json.load(json_file)


def get_news_article(link):
    for article in get_news_articles():
        if article["link"] == link:
            return article
    return None


def get_news_articles_sorted_by_date(newer_first=True):
    return __sort_articles_by_date(get_news_articles(), newer_first)


def __sort_articles_by_date(articles, newer_first=True):
    articles.sort(key=lambda v: v["created"])
    if newer_first:
        articles.reverse()
    sorted_articles = []

    for i in range(len(articles)):
        date = articles[i]["created"][:10]
        if i == 0 or not articles[i - 1]["created"].startswith(date):
            sorted_articles.append((date, [articles[i]]))
        else:
            sorted_articles[-1][1].append(articles[i])

    return sorted_articles
