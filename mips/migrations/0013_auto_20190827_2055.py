# Generated by Django 2.2.2 on 2019-08-28 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mips', '0012_auto_20190827_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_main_image',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_preface',
            field=models.TextField(default=''),
        ),
    ]
