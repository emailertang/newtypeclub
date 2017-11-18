# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    address = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=10,null=True)
    state_provice = models.CharField(max_length=10,null=True)
    contry = models.CharField(max_length=10,null=True)
    website = models.CharField(max_length=40,null=True)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
<<<<<<< HEAD
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    book_info = models.OneToOneField('Book_info',null=True)
=======
    authors = models.ManyToManyField(Auther,null=True)
    publisher = models.ForeignKey(Publisher,null=True)
    publication_date = models.DateField(auto_now_add=True)
>>>>>>> b21642d7f09f5f0b40bf0c91777557bfe5fd07ee
    def __str__(self):
        return self.title
class Book_info(models.Model):
    isdn = models.IntegerField(unique=True, null=True)
    price = models.IntegerField(null=True)




