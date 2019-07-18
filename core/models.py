from django.db import models
from django.contrib.auth.models import User
import tagulous


class Responder(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, blank=False, null=False)
    gender = models.CharField(max_length=10, blank=False)
    age = models.CharField(max_length=10, blank=False)
    relation = models.CharField(max_length=20, blank=False)
    words = tagulous.models.TagField(
        force_lowercase=True,
        max_count=10,
    )

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.code

#
# class Tag(models.Model):
#     word = models.CharField(max_length=50)
#     editdate = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ('word',)
#
#     def __str__(self):
#         return self.word
