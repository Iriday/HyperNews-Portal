from django.db import models
from HyperNews_Portal.settings import NEWS_JSON_PATH
import json


def get_news_articles():
    with open(NEWS_JSON_PATH, "r") as json_file:
        return json.load(json_file)


def get_news_article(link):
    return get_news_articles()[link - 1]  # if link = 0 returns the newest article
