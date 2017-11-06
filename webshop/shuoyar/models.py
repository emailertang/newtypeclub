# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.
class shuoyarStudent(models.Model):
    sid = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(null=True)
    class Meta:
        db_table = "Student"
    def __str__(self):
        return self.name

