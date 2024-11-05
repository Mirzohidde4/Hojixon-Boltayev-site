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
        verbose_name = 'Asosiy sahifa'
        verbose_name_plural = 'Asosiy sahifa'


class Biografiya(models.Model):
    name = models.CharField(max_length=100, verbose_name='ismi')
    description = models.CharField(max_length=100, verbose_name='qisqacha')
    bio = models.TextField(verbose_name="ma'lumot")
    add = models.TextField(verbose_name="qo'shimcha", blank=True, null=True)
    image = models.ImageField(upload_to='images/', verbose_name='rasm')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Batafsil'
        verbose_name_plural = 'Batafsil'


class Add(models.Model):
    name = models.CharField(max_length=100, verbose_name='ismi')
    description = models.CharField(max_length=100, verbose_name='qisqacha')
    bio = models.TextField(verbose_name="ma'lumot")
    image = models.ImageField(upload_to='images/', verbose_name='rasm')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Qo'shimcha"
        verbose_name_plural = "Qo'shimcha"
    

class Site(models.Model):
    title = models.CharField(max_length=100, verbose_name='nomi')
    icon = models.ImageField(upload_to='images/', verbose_name='belgisi')
    name = models.CharField(verbose_name='ismi', max_length=100)
    description = models.CharField(verbose_name='qisqacha', max_length=100)

    class Meta:
        verbose_name = "Web sayt"
        verbose_name_plural = "Web sayt"    


class Comments(models.Model):
    author = models.CharField(max_length=100, verbose_name='fordalanuvchi')
    comment = models.TextField(verbose_name='izohi')
    created = models.DateTimeField(auto_now_add=True, verbose_name='yuborilgan sana')

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"