# Generated by Django 3.1.7 on 2021-04-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholorship_app', '0003_scholorship_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholorship',
            name='datetime',
            field=models.DateField(default='2021-04-30'),
        ),
    ]