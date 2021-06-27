from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("article", views.article, name="article"),
    path("edit_article", views.edit_article, name="edit_article"),
]
