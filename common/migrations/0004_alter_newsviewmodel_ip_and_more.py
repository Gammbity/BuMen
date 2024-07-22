# Generated by Django 5.0.6 on 2024-07-22 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_newsviewmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsviewmodel',
            name='ip',
            field=models.GenericIPAddressField(db_index=True),
        ),
        migrations.AlterField(
            model_name='newsviewmodel',
            name='visitor_id',
            field=models.UUIDField(db_index=True),
        ),
    ]
