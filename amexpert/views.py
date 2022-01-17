from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.utils import timezone

from amexpert.models import Event, Post, Member
from amexpert.forms import NewMemberForm

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


class MemberShipCreated(View):
    template_name = "amexpert/website/membership_created.html"
    def get(self, request):
        return render(request, self.template_name)


class NewMemberShipView(View):
    template_name = "amexpert/website/new_membership.html"

    def get(self, request):
        form = NewMemberForm()

        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = NewMemberForm(request.POST)
           # check whether it's valid:
        if form.is_valid():
           # process the data in form.cleaned_data as required
           # ...
           # redirect to a new URL:
           member = Member(
               fullname = form.cleaned_data['fullname'],
               email = form.cleaned_data['email'],
               linkedin = form.cleaned_data['linkedin'],
               github = form.cleaned_data['github'],
               website = form.cleaned_data['website'],
               bio = form.cleaned_data['bio'],
               pronouns = form.cleaned_data['pronouns']
           )
           member.save()
           
           return HttpResponseRedirect('/membership-created')
