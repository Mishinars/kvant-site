from django.db import models

class New(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    text = models.TextField()

class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='default_image.jpg')
    event_dates = models.DateField()
    min_age = models.IntegerField(default=0)
    max_age = models.IntegerField(default=18)
    comment = models.TextField()

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')

class Raspisanie(models.Model):
    image = models.ImageField(upload_to='images/')
