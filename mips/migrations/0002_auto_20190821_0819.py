# Generated by Django 2.2.2 on 2019-08-21 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mips', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AlterModelOptions(
            name='lessonparagraph',
            options={'verbose_name': 'Lesson Paragraph', 'verbose_name_plural': 'Lesson Paragraphs'},
        ),
    ]
