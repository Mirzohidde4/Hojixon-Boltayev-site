# Generated by Django 5.1.2 on 2024-11-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_add_options_alter_biografiya_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='permission',
        ),
        migrations.AddField(
            model_name='site',
            name='permission',
            field=models.CharField(default=2, max_length=200, verbose_name='izoh qoldirish uchun'),
            preserve_default=False,
        ),
    ]
