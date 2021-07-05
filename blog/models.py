from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone

class Article(models.Model):
    title = models.CharField('Title', max_length=200)
    image = models.ImageField(upload_to="uploads/images/articles")
    summary = models.TextField()
    tags = models.CharField(max_length=300, default="")
    created_at = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    slug = models.CharField(max_length=300, unique=True)
    text = CKEditor5Field('Text', config_name='extends')

    def save(self) -> None:
        self.slug = "-".join(self.title.lower().split())
        return super().save()

    def __str__(self) -> str:
        return f"{self.id}. {self.title}"
