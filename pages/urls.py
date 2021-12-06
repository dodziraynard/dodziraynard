from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("<str:page_id>/<str:slug>", views.pages, name="pages"),
]
