# Generated by Django 5.0.6 on 2024-07-29 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_remove_lessonthememodel_title_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testquestionchoicemodel',
            old_name='text',
            new_name='choice',
        ),
        migrations.RenameField(
            model_name='testquestionchoicemodel',
            old_name='text_en',
            new_name='choice_en',
        ),
        migrations.RenameField(
            model_name='testquestionchoicemodel',
            old_name='text_ru',
            new_name='choice_ru',
        ),
        migrations.RenameField(
            model_name='testquestionchoicemodel',
            old_name='text_uz',
            new_name='choice_uz',
        ),
    ]
