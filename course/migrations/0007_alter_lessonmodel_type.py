# Generated by Django 5.0.6 on 2024-07-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_rename_text_testquestionchoicemodel_choice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonmodel',
            name='type',
            field=models.IntegerField(choices=[(1, 'mahalliy'), (2, 'umumjahon')], max_length=100, verbose_name='turi'),
        ),
    ]
