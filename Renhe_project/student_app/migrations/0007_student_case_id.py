# Generated by Django 3.1.7 on 2021-05-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0006_remove_student_case_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='case_id',
            field=models.CharField(default='無', max_length=256, verbose_name='案號'),
        ),
    ]
