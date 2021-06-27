from django.shortcuts import redirect, render
from . models import Article


def index(request):
    template_name = 'blog/index.html'

    if request.method == "POST":
        text = request.POST.get("text")
        id = request.POST.get("id")
        if id:
            Article.objects.filter(id=id).update(
                title="POST 1 on Django", text=text
            )
        else:
            Article.objects.create(title="POST 1 on Django", text=text)
        
        return redirect("blog:index")
    context = {
        "articles":Article.objects.all(),
        "article":Article.objects.last(),
    }
    return render(request, template_name, context)



def edit_article(request):
    template_name = 'blog/edit_article.html'
    context = {
        "article":Article.objects.last(),
    }
    return render(request, template_name, context)


def article(request):
    template_name = "blog/article.html"

    context = {
        "article":Article.objects.last(),
    }
    return render(request, template_name, context)