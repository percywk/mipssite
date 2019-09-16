# Generated by Django 2.2.2 on 2019-08-21 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mips', '0005_auto_20190821_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessonnavigation',
            name='lesson',
        ),
        migrations.AlterField(
            model_name='lessonnavigation',
            name='associatedParagraph',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mips.LessonParagraph'),
        ),
    ]