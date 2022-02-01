from django.contrib import admin

from .models import Event, Member, Post, Speaker, Sponser

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Sponser)
admin.site.register(Post)
admin.site.register(Member)