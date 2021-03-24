from django.db import models

# Create your models here.
class Article(models.Model):
    """Model definition for Article."""

    title = models.CharField(max_length=50)
    url_image = models.URLField(max_length=200)
    description = models.TextField()
    source = models.CharField(max_length=50)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.title

