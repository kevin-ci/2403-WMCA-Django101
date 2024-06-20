from django.urls import path
from . import views


urlpatterns = [
    path("home", views.news_home, name="news_home"),
    path("create", views.create_article, name="create_article"),
    path("edit/<article_id>", views.edit_article, name="edit_article"),
    path("delete/<article_id>", views.delete_article, name="delete_article"),
    path("mine", views.your_articles, name="your_articles"),
    path("written_by/<author_id>", views.articles_by_author, name="by_author"),
    path("<article_id>", views.view_article, name="view_article"),
]