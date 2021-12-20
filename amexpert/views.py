from django.shortcuts import get_object_or_404, render
from django.views import View
from django.utils import timezone

from amexpert.models import Event


class IndexView(View):
    template_name = "amexpert/index.html"

    def get(self, request):
        return render(request, self.template_name)


class EventsView(View):
    template_name = "amexpert/events.html"

    def get(self, request):
        events = Event.objects.filter(visible=True,
                                      timestamp__gte=timezone.now())
        context = {"events": events}
        return render(request, self.template_name, context)


class EventDetailView(View):
    template_name = "amexpert/event_detail.html"

    def get(self, request, event_id, **kwargs):
        event = get_object_or_404(Event, id=event_id)
        context = {"event": event}
        return render(request, self.template_name, context)
