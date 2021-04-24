# Generated by Django 3.1.7 on 2021-04-24 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='case',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='is_scholorship',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='case',
            name='scholorship_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='situation',
            field=models.TextField(default='無', max_length=512),
        ),
        migrations.AddField(
            model_name='case',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='total_money',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='visited_form',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='visited_photos',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='contribute_context',
            field=models.TextField(max_length=256),
        ),
    ]
