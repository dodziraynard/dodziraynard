from random import choice
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone
from django.contrib.auth.models import User


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
    slug = models.CharField(max_length=250)
    registration_link = models.URLField(blank=True, null=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, **kwargs) -> None:
        self.slug = "-".join(self.title.lower().split())
        return super().save(**kwargs)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    title = models.CharField('Title', max_length=200)
    image = models.ImageField(upload_to="uploads/images/articles")
    abstract = models.TextField()
    tags = models.CharField(max_length=300, default="")
    published = models.BooleanField(default=False)
    slug = models.CharField(max_length=300, unique=True)
    content = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)

    def save(self) -> None:
        self.slug = "-".join(self.title.lower().split())
        return super().save()

    def __str__(self) -> str:
        return f"{self.id}. {self.title}"
    
class Member(models.Model):
    PRONOUNS= [
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Miss', 'Miss'),
        ('Sir', 'Sir'),
        ('Madam', 'Madam')
    ]
    fullname = models.CharField(max_length=200)
    email = models.EmailField(null=False, max_length=200)
    photo = models.ImageField(null=True, upload_to= 'uploads/images/members', blank=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    bio = CKEditor5Field(blank=True)
    pronouns = models.CharField(max_length=100, null=True, blank=True, choices=PRONOUNS)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False,)
    update_at = models.DateTimeField(auto_now=True, null=False)
    visible = models.BooleanField(default=True)
    slug = models.CharField(max_length=250)

    def save(self, **kwargs) -> None:
        self.slug = "-".join(self.fullname.lower().split())
        return super().save(**kwargs)

    def __str__(self) -> str:
        return self.fullname
