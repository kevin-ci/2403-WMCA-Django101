from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.http import HttpResponse
from .forms import ArticleForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def view_article(request, article_id):
    retrieved_article = Article.objects.get(id=article_id)

    context = {
        'article': retrieved_article,
        'author': "Kevin Loughrey",
    }

    return render(request, 'articles/article.html', context)


def news_home(request):
    all_articles = Article.objects.all()
    context = { "articles": all_articles }
    return render(request, 'articles/all_articles.html', context)


def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article_form = form.save(commit=False)
            article_form.author = request.user
            article_form.save()
            return redirect("news_home")

    else:
        form = ArticleForm()
        context = { "form": form }
        return render(request, 'articles/create_article.html', context)

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if article.author != request.user:
        return HttpResponse("You can't edit an article you didn't create!")

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article_form = form.save(commit=False)
            article_form.author = request.user
            article_form.save()
            return redirect("news_home")
    else:
        form = ArticleForm(instance=article)
        context = { "form": form }
        return render(request, 'articles/edit_article.html', context)


@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if article.author != request.user:
        return HttpResponse("You can't delete an article you didn't create!")

    if request.method == "POST":
        article.delete()
        return redirect('news_home')
    else:
        context = { "article_id": article_id }
        return render(request, 'articles/delete_article.html', context)
 


@login_required
def your_articles(request):
    your_articles = Article.objects.filter(author=request.user)
    context = { "articles": your_articles }
    return render(request, 'articles/all_articles.html', context)


def articles_by_author(request, author_id):
    articles = Article.objects.filter(author=author_id)
    user = User.objects.get(id=author_id)
    context = { "articles": articles, "user": user }
    return render(request, 'articles/articles_by_author.html', context)