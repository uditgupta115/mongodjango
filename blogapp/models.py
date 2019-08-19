from django.conf import settings
from django.db import models
from mongoengine import *

from mongodjango.settings import DBNAME

# Create your models here.

connect(DBNAME)


class Post(DynamicDocument):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)

    def __str__(self):
        return self.title


class Status(models.Model):
    profile = models.ManyToManyField('Account')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return str(self.user)


class Account(models.Model):
    profile_status = models.ManyToManyField(Status, blank=True)

    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_query_name='user_model'
    )

    def __str__(self):
        return str(self.user.filter().last().username)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ('headline',)

    def __str__(self):
        return self.headline
