from django.db.models import query
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article


def index(request):
    template_name = 'blog/index.html'

    query = request.GET.get("query", "")
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(tags__icontains=query)
            | Q(text__icontains=query))
    else:
        articles = Article.objects.all()

    if not request.user.is_staff:
        articles = articles.filter(published=True)

    context = {
        "articles": articles.order_by("-created_at")[:20],
        "query": query,
    }
    return render(request, template_name, context)


def store_article(request):
    if request.method == "POST":
        text = request.POST.get("text")
        title = request.POST.get("title")
        published = 'on' in request.POST.get("published", "")

        id = request.POST.get("id")
        if id:
            Article.objects.filter(id=id).update(title=title,
                                                 text=text,
                                                 published=published)
        else:
            Article.objects.create(title=title, text=text, published=published)

        return redirect("blog:index")


def edit_article(request, slug, article_id):
    article = get_object_or_404(Article, id=article_id)

    template_name = 'blog/edit_article.html'
    context = {
        "article": article,
    }
    return render(request, template_name, context)


def article(request, slug, article_id):
    template_name = "blog/article.html"
    article = get_object_or_404(Article, id=article_id)
    articles = Article.objects.filter(tags__in=article.tags.split()).exclude(
        id=article.id)

    if not request.user.is_staff:
        articles = articles.filter(published=True)

    context = {
        "article": article,
        "articles": articles,
    }
    return render(request, template_name, context)