# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=10,null=True)
    state_provice = models.CharField(max_length=10,null=True)
    contry = models.CharField(max_length=10,null=True)
    website = models.CharField(max_length=40,null=True)
    def __str__(self):
        return self.name

class Auther(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Auther,null=True)
    publisher = models.ForeignKey(Publisher,null=True)
    publication_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title



