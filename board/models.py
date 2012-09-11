from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    user = models.ForeignKey(User)
