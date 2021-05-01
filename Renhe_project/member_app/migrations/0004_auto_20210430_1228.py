# Generated by Django 3.1.7 on 2021-04-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0003_auto_20210430_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(default='', max_length=256, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='member',
            name='created_at',
            field=models.DateField(default='2021-04-30', verbose_name='加入日期'),
        ),
        migrations.AlterField(
            model_name='member',
            name='expired_at',
            field=models.DateField(default='2021-04-30', verbose_name='會員失效日期'),
        ),
        migrations.AlterField(
            model_name='member',
            name='id_number',
            field=models.CharField(max_length=256, verbose_name='身分證'),
        ),
        migrations.AlterField(
            model_name='member',
            name='intro_by',
            field=models.CharField(blank=True, default='無', max_length=256, verbose_name='介紹人'),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_donate',
            field=models.BooleanField(default=False, verbose_name='會費繳納'),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_member_now',
            field=models.BooleanField(default=True, verbose_name='會員身份'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=256, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=256, verbose_name='電話'),
        ),
        migrations.AlterField(
            model_name='member',
            name='title',
            field=models.CharField(default='一般會員', max_length=256, verbose_name='職位'),
        ),
    ]
