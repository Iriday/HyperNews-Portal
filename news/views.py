from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, Http404
from news.models import get_news_article, sort_articles_by_date, get_news_articles, add_news_article


class MainView(View):
    def get(self, request, *args, **kwargs):
        return redirect("/news/")


class NewsArticleView(View):
    def get(self, request, link, *args, **kwargs):
        article = get_news_article(int(link))
        if not article:
            raise Http404

        return render(request, "news/article.html", context={"article": article})


class NewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "news/news.html",
                      context={"sorted_articles": sort_articles_by_date(get_news_articles(request.GET.get('q')))})


class CreateNewsArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "news/create_article.html")

    def post(self, request, *args, **kwargs):
        add_news_article(request.POST['title'], request.POST['text'])
        return redirect("/news/")
