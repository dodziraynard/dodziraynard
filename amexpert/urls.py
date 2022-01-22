from django.urls import path

from . import views

app_name = "amexpert"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("amexpert", views.IndexView.as_view(), name="amexpert"),
    path("new-membership",
         views.NewMemberShipView.as_view(),
         name="new_membership"),
    path("membership-created",
         views.MemberShipCreated.as_view(),
         name="membership_created"),
    path("events", views.EventsView.as_view(), name="events"),
    path("events/<str:event_id>/<str:slug>",
         views.EventDetailView.as_view(),
         name="event_detail"),
    path("post/<str:post_id>/<str:slug>",
         views.PostDetailView.as_view(),
         name="post_detail"),
]
