# Generated by Django 3.1.7 on 2021-04-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0002_auto_20210424_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='memo',
            field=models.TextField(max_length=512, verbose_name='備註'),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=256, verbose_name='校名'),
        ),
        migrations.AlterField(
            model_name='school',
            name='represent_person_name',
            field=models.CharField(max_length=256, verbose_name='負責人'),
        ),
        migrations.AlterField(
            model_name='school',
            name='represent_person_phone',
            field=models.CharField(max_length=256, verbose_name='負責人電話'),
        ),
    ]
