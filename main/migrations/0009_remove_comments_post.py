# Generated by Django 5.1.2 on 2024-11-04 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_comments_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
    ]
