from django.conf import settings
from django.db import models
from django.utils import timezone


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title