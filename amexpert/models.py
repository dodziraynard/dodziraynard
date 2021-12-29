from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Speaker(models.Model):
    fullname = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="uploads")
    linkedin = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    bio = CKEditor5Field()
    pronouns = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)
    slug = models.CharField(max_length=250)

    def save(self, **kwargs) -> None:
        self.slug = "-".join(self.fullname.lower().split())
        return super().save(**kwargs)

    def __str__(self) -> str:
        return self.fullname


class Sponser(models.Model):
    fullname = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="uploads")
    about = CKEditor5Field()
    website = models.URLField()
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=250)

    def save(self, **kwargs) -> None:
        self.slug = "-".join(self.fullname.lower().split())
        return super().save(**kwargs)

    def __str__(self) -> str:
        return self.fullname


class Event(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    details = CKEditor5Field()
    abstract = models.TextField()
    banner = models.ImageField(upload_to="uploads")
    small_banner = models.ImageField(upload_to="uploads",
                                     null=True,
                                     blank=True)
    timestamp = models.DateTimeField()
    sponsors = models.ManyToManyField(Sponser)
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
