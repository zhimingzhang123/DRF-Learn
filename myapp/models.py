from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=10)
    ct = models.ForeignKey("City", on_delete=models.CASCADE,null=True,blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=10)
    ta = models.ManyToManyField('Tag', related_name='tag_many')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=10)
    art = models.ManyToManyField('Article', related_name='art_many')

    def __str__(self):
        return self.name

