from django.db import models
from HyperNews_Portal.settings import NEWS_JSON_PATH
import datetime
import json


def get_news_articles(q=None):
    articles = __read_articles_from_file(NEWS_JSON_PATH)
    return articles if not q else list(filter(lambda a: q in a['title'], articles))


def get_news_article(link):
    for article in get_news_articles():
        if article["link"] == link:
            return article
    return None


def add_news_article(title, text):
    articles = get_news_articles()
    articles.append({"created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                     "title": title,
                     "text": text,
                     "link": max(articles, key=lambda a: a['link'])['link'] + 1})
    __save_articles_to_file(articles, NEWS_JSON_PATH)


def sort_articles_by_date(articles, newer_first=True):
    articles.sort(key=lambda v: v["created"])
    if newer_first:
        articles.reverse()
    sorted_articles = {}

    for article in articles:
        sorted_articles.setdefault(article["created"][:10], []).append(article)

    return sorted_articles.items()


def __read_articles_from_file(path):
    with open(path, "r") as json_file:
        return json.load(json_file)


def __save_articles_to_file(articles, path):
    with open(path, 'w') as json_file:
        json.dump(articles, json_file)
