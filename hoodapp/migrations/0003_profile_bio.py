# Generated by Django 4.0.5 on 2022-06-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]