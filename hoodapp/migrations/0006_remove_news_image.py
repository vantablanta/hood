# Generated by Django 4.0.5 on 2022-06-18 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0005_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
    ]
