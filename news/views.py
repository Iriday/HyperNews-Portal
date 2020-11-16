from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404
from django.http.response import HttpResponseBadRequest
from news.models import get_news_article


class MainView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Coming soon</h1>")


class NewsArticleView(View):
    def get(self, request, link, *args, **kwargs):
        try:
            context = {"article": get_news_article(int(link))}
        except IndexError:
            raise Http404

        return render(request, "news/article.html", context=context)  # if link = 0 returns the newest article
