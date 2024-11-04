from django.db import models

# Create your models here.
class Index(models.Model):
    name = models.CharField(verbose_name='ism', max_length=100)
    year = models.CharField(verbose_name='yil', max_length=100)
    info = models.TextField(verbose_name='info')
    image = models.ImageField(verbose_name='rasm', upload_to='images/')

    def __str__(self):
        return self.name


class Biografiya(models.Model):
    name = models.CharField(max_length=100, verbose_name='ism')
    description = models.CharField(max_length=100, verbose_name='description')
    bio = models.TextField(verbose_name='info')
    add = models.TextField(verbose_name='add', blank=True, null=True)
    image = models.ImageField(upload_to='images/', verbose_name='rasm')

    def __str__(self):
        return self.name


class Add(models.Model):
    name = models.CharField(max_length=100, verbose_name='ism')
    description = models.CharField(max_length=100, verbose_name='description')
    bio = models.TextField(verbose_name='info')
    image = models.ImageField(upload_to='images/', verbose_name='rasm')

    def __str__(self):
        return self.name
    

class Site(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    icon = models.ImageField(upload_to='images/', verbose_name='rasm')
    name = models.CharField(verbose_name='ism', max_length=100)
    description = models.CharField(verbose_name='des', max_length=100)    