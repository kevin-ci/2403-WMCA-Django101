from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="articles"
    )