from django.shortcuts import get_object_or_404, render
from .models import Page


def pages(request, page_id, **kwargs):
    template_name = "pages/page.html"
    page = get_object_or_404(Page, id=page_id)
    context = {"page": page}
    return render(request, template_name, context)