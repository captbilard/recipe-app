# Generated by Django 3.0.8 on 2020-07-22 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20200722_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='meals',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
