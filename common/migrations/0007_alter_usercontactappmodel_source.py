# Generated by Django 5.0.6 on 2024-07-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_usercontactappmodel_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontactappmodel',
            name='source',
            field=models.CharField(choices=[('mobile', 1), (2, 'landing')], max_length=255),
        ),
    ]
