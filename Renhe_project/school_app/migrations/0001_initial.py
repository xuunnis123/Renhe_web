# Generated by Django 3.1.7 on 2021-04-23 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('represent_person_name', models.CharField(max_length=256)),
                ('represent_person_phone', models.CharField(max_length=256)),
                ('memo', models.CharField(max_length=256)),
            ],
        ),
    ]
