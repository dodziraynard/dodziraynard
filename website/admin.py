from django.contrib import admin
from .models import Project, ProjectImage, TnC

admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(TnC)