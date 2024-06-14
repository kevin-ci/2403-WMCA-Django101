from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def view_article(request, article_id):
    retrieved_article = Article.objects.get(id=article_id)

    context = {
        'article': retrieved_article,
        'author': "Kevin Loughrey",
    }

    return render(request, 'articles/article.html', context)


def news_home(request):
    return HttpResponse("News Homepage Goes Here")