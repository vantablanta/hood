# Generated by Django 4.0.5 on 2022-06-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0007_business'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.CharField(max_length=300),
        ),
    ]
