from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(null=True, blank=True)
    preview_link = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project,
                                related_name='images',
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/images/articles")
    is_main = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.project.title
