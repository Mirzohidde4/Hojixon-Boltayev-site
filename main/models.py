from django.db import models

# Create your models here.
class Index(models.Model):
    name = models.CharField(verbose_name='ismi', max_length=100)
    year = models.CharField(verbose_name='yili', max_length=100)
    info = models.TextField(verbose_name="ma'lumot")
    image = models.ImageField(verbose_name='rasm', upload_to='images/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '1-sahifa'
        verbose_name_plural = '1-sahifa'


class Biografiya(models.Model):
    name = models.CharField(max_length=100, verbose_name='ismi')
    description = models.CharField(max_length=100, verbose_name='qisqacha')
    bio = models.TextField(verbose_name="ma'lumot")
    add = models.TextField(verbose_name="qo'shimcha", blank=True, null=True)
    image = models.ImageField(upload_to='images/', verbose_name='rasm')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '2-sahifa'
        verbose_name_plural = '2-sahifa'


class Add(models.Model):
    name = models.CharField(max_length=100, verbose_name='ismi')
    description = models.CharField(max_length=100, verbose_name='qisqacha')
    bio = models.TextField(verbose_name="ma'lumot")
    image = models.ImageField(upload_to='images/', verbose_name='rasm')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "3-sahifa"
        verbose_name_plural = "3-sahifa"
    

class Site(models.Model):
    title = models.CharField(max_length=100, verbose_name='nomi')
    icon = models.ImageField(upload_to='images/', verbose_name='belgisi')
    name = models.CharField(verbose_name='ismi', max_length=100)
    description = models.CharField(verbose_name='qisqacha', max_length=100)
    page1 = models.CharField(max_length=100, verbose_name='1-sahifa')
    page2 = models.CharField(max_length=100, verbose_name='2-sahifa')
    page3 = models.CharField(max_length=100, verbose_name='3-sahifa')
    page4 = models.CharField(max_length=100, verbose_name='4-sahifa')

    class Meta:
        verbose_name = "4-sahifa"
        verbose_name_plural = "4-sahifa"    


class Comments(models.Model):
    author = models.CharField(max_length=100, verbose_name='fordalanuvchi')
    comment = models.TextField(verbose_name='izohi')
    created = models.DateTimeField(auto_now_add=True, verbose_name='yuborilgan sana')

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"