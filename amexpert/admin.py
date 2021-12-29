from django.contrib import admin
from .models import Event, Speaker, Sponser, Post

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Sponser)
admin.site.register(Post)