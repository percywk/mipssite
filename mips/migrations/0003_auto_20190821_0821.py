# Generated by Django 2.2.2 on 2019-08-21 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mips', '0002_auto_20190821_0819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessonnavigation',
            options={'verbose_name': 'Lesson Navigation', 'verbose_name_plural': 'Lesson Navigations'},
        ),
        migrations.AlterModelOptions(
            name='lessonparagaphimage',
            options={'verbose_name': 'Lesson Paragraph Image', 'verbose_name_plural': 'Lesson Paragraph Images'},
        ),
    ]
