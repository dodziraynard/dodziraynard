from django.urls import path
from . import views

app_name = "amexpert"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("events", views.EventsView.as_view(), name="events"),
    path("events/<str:event_id>/<str:slug>",
         views.EventDetailView.as_view(),
         name="detail_details"),
]
