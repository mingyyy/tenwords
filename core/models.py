from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):

    word = models.CharField(max_length=50)

    class Meta:
        ordering = ('word',)

    def __str__(self):
        return self.word


class Responder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    word = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

