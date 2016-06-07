from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    body = models.TextField()
