# Generated by Django 3.1 on 2020-12-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
