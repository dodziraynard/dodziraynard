from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Speaker(models.Model):
    fullname = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="uploads")
    pronouns = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)
    bio = CKEditor5Field()
    visible = models.BooleanField(default=True)
    slug = models.CharField(max_length=250)

    def save(self, **kwargs) -> None:
        self.slug = "-".join(self.title.lower().split())
        return super().save(**kwargs)

    def __str__(self) -> str:
        return self.fullname


class Event(models.Model):
    title = models.CharField(max_length=200)
    details = CKEditor5Field()
    banner = models.ImageField(upload_to="uploads")
    timestamp = models.DateTimeField()
    speakers = models.ManyToManyField(Speaker)
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=250)
    visible = models.BooleanField(default=True)

    def save(self, **kwargs) -> None:
        self.slug = "-".join(self.title.lower().split())
        return super().save(**kwargs)

    def __str__(self) -> str:
        return self.title
