from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Page(models.Model):
    title = models.CharField('Title', max_length=200)
    content = CKEditor5Field('Text', config_name='extends')
    summary = models.TextField()
    image = models.ImageField(upload_to="uploads", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    slug = models.CharField(max_length=300, unique=True)

    def save(self) -> None:
        self.slug = "-".join(self.title.lower().split())
        return super().save()

    def __str__(self) -> str:
        return f"{self.id}. {self.title}"


class TnC(models.Model):
    title = models.CharField(max_length=200)
    text = CKEditor5Field()

    def __str__(self) -> str:
        return self.title