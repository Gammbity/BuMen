# Generated by Django 5.0.6 on 2024-07-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_lessonmodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlessonmodel',
            name='last_seen_at',
            field=models.DateTimeField(auto_now=True, verbose_name="so'nggi ko'rilgan"),
        ),
    ]
