# -*- coding: UTF-8 -*-
from django.db import models


# Create your models here.
class Blog(models.Model):
  name = models.CharField(max_length=100)
  time =models.DateTimeField()
  content = models.TextField()

  def __unicode__(self):  # __str__ on Python 3
    return self.name


class Author(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()

  def __unicode__(self):  # __str__ on Python 3
    return self.name
