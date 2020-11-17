from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404
from news.models import get_news_article, get_news_articles_sorted_by_date


class MainView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Coming soon</h1>")


class NewsArticleView(View):
    def get(self, request, link, *args, **kwargs):
        article = get_news_article(int(link))
        if not article:
            raise Http404

        return render(request, "news/article.html", context={"article": article})


class NewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "news/news.html", context={"sorted_articles": get_news_articles_sorted_by_date()})
