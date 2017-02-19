from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tags(models.Model):
	tag = models.CharField(max_length=50)

class Comment(models.Model):
	comment = models.CharField(max_length=200)

class Photo(models.Model):
	link = models.CharField(max_length=200)
	likes = models.IntegerField()
	time = models.DateTimeField(null=True)
	comments = models.ManyToManyField(Comment, null=True)
	tag = models.ManyToManyField(Tags, null=True)

class InstagramAccount(models.Model):
	username = models.CharField(max_length=20)
	photo = models.ManyToManyField(Photo, null=True)
