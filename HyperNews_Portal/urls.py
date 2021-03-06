"""HyperNews_Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from news.views import MainView, NewsArticleView, NewsView, CreateNewsArticleView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', NewsView.as_view()),
    path('news/create/', CreateNewsArticleView.as_view()),
    re_path('news/[?]q=(?P<q>[^/]+)/?', NewsView.as_view()),
    re_path('news/(?P<link>[0-9]+)/?', NewsArticleView.as_view()),
    path('', MainView.as_view())
]
urlpatterns += static(settings.STATIC_URL)
