from django.urls import path
from . import views


urlpatterns = [
    path("home", views.news_home, name="news_home"),
    path("<article_id>", views.view_article, name="view_article"),
]