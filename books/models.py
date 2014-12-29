#-*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class BookManager(models.Manager):
    def get_or_create(self, **kwargs):
        defaults = kwargs.pop('defaults', {})
        author_list = defaults.pop('author_list', {})
        Book.author_list = author_list
        kwargs.update(defaults)
        super(BookManager, self).get_or_create(**kwargs)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author,related_name="translater")
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    def __unicode__(self):
        return self.title
