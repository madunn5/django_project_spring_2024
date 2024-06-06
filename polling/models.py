from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title
