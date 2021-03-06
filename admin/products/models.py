from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    name = models.CharField(max_length=200, default='John Doe')
    email = models.CharField(max_length=200, default='johndoe@nomail.com')
