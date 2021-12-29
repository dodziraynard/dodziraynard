from django.urls import path
from . import views

app_name = "amexpert"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("events", views.EventsView.as_view(), name="events"),
    path("events/<str:event_id>/<str:slug>",
         views.EventDetailView.as_view(),
         name="event_detail"),
    path("post/<str:post_id>/<str:slug>",
         views.PostDetailView.as_view(),
         name="post_detail"),
]
