from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    age = models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class New(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    image =  models.ImageField(upload_to='images/')
    text = models.TextField()

class Event(models.Model):
    title = models.CharField(max_length=255)
    target_audience = models.CharField(max_length=255)
    event_dates = models.DateField()
    responsible_institution = models.CharField(max_length=255)
    comment = models.TextField()

class Connection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    news = models.ForeignKey(New, on_delete=models.CASCADE)

