# Generated by Django 5.0.7 on 2024-09-05 08:02

from django.db import migrations, models #type:ignore


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='read',
            name='humidity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='read',
            name='temp',
            field=models.IntegerField(default=0),
        ),
    ]
