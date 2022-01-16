from django.shortcuts import get_object_or_404, render
from django.views import View
from django.utils import timezone

from amexpert.models import Event, Post


class IndexView(View):
    template_name = "amexpert/website/index.html"

    def get(self, request):
        event = Event.objects.filter(
            timestamp__gte=timezone.now()).order_by("timestamp").first()
        posts = Post.objects.filter(published=True)
        context = {
            "event": event,
            "posts": posts,
        }
        return render(request, self.template_name, context)


# class IndexView(View):
#     template_name = "amexpert/events/index.html"

#     def get(self, request):
#         event = Event.objects.filter(
#             timestamp__gte=timezone.now()).order_by("timestamp").first()
#         posts = Post.objects.filter(published=True)
#         context = {
#             "event": event,
#             "posts": posts,
#         }
#         return render(request, self.template_name, context)


class EventsView(View):
    template_name = "amexpert/events/events.html"

    def get(self, request):
        events = Event.objects.filter(visible=True,
                                      timestamp__gte=timezone.now())
        context = {"events": events}
        return render(request, self.template_name, context)


class EventDetailView(View):
    template_name = "amexpert/events/event_detail.html"

    def get(self, request, event_id, **kwargs):
        event = get_object_or_404(Event, id=event_id)
        context = {"event": event}
        return render(request, self.template_name, context)


class PostDetailView(View):
    template_name = "amexpert/events/post_detail.html"

    def get(self, request, post_id, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        context = {"post": post}
        return render(request, self.template_name, context)


class NewMemberShipView(View):
    template_name = "amexpert/website/new_membership.html"

    def get(self, request):
        return render(request, self.template_name)
