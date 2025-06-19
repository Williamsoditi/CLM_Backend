from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.
class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, help_text="A unique identifier for the URL. Will be auto-generated from the title.")
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField(
        'News Image',
        blank=True,
        null=True,
        help_text="Optional image for the news article."
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date'] 