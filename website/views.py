from django.shortcuts import render

from blog.models import Article

from .models import Project


def index(request):
    template_name = "website/index.html"
    articles = Article.objects.filter()
    if not request.user.is_staff:
        articles = articles.filter(published=True)

    context = {
        "articles": articles,
    }
    return render(request, template_name, context)


def projects(request):
    template_name = "website/projects.html"
    projects = Project.objects.filter()

    context = {
        "projects": projects,
    }
    return render(request, template_name, context)