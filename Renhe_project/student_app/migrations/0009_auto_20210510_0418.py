# Generated by Django 3.1.7 on 2021-05-10 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0008_auto_20210509_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='content',
        ),
        migrations.AlterField(
            model_name='student',
            name='end_date',
            field=models.DateField(blank=True, default='2021-05-10', verbose_name='個案結束日期'),
        ),
        migrations.AlterField(
            model_name='student',
            name='start_date',
            field=models.DateField(default='2021-05-10', verbose_name='個案開始日期'),
        ),
    ]
