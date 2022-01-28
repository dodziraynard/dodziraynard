from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("store_article", views.store_article, name="store_article"),
    path("article/<str:slug>/<int:article_id>", views.article, name="article"),
    path("edit_article/<str:slug>/<int:article_id>", views.edit_article, name="edit_article"),
]
