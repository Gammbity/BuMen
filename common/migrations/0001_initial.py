# Generated by Django 5.0.6 on 2024-07-28 12:33

import ckeditor_uploader.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAppModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('caption', models.CharField(max_length=255)),
                ('caption_en', models.CharField(max_length=255, null=True)),
                ('caption_uz', models.CharField(max_length=255, null=True)),
                ('caption_ru', models.CharField(max_length=255, null=True)),
                ('text', models.TextField()),
                ('text_en', models.TextField(null=True)),
                ('text_uz', models.TextField(null=True)),
                ('text_ru', models.TextField(null=True)),
                ('order', models.PositiveIntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'about app',
                'verbose_name_plural': 'advertisements',
            },
        ),
        migrations.CreateModel(
            name='AdvertisingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('image', models.ImageField(upload_to='advertising/%Y/%m/')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'advertising',
                'verbose_name_plural': 'advertisements',
            },
        ),
        migrations.CreateModel(
            name='ContactCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('title', models.CharField(max_length=255, verbose_name='nomi')),
            ],
            options={
                'verbose_name': 'contact category',
                'verbose_name_plural': 'contact categories',
            },
        ),
        migrations.CreateModel(
            name='FAQModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('question', models.CharField(max_length=255)),
                ('question_en', models.CharField(max_length=255, null=True)),
                ('question_uz', models.CharField(max_length=255, null=True)),
                ('question_ru', models.CharField(max_length=255, null=True)),
                ('answer', models.CharField(max_length=255)),
                ('answer_en', models.CharField(max_length=255, null=True)),
                ('answer_uz', models.CharField(max_length=255, null=True)),
                ('answer_ru', models.CharField(max_length=255, null=True)),
                ('order', models.PositiveIntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
                'ordering': ['order', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='NewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('banner', models.ImageField(upload_to='common/news/%Y/%m/')),
                ('top', models.BooleanField(default=False)),
                ('hit_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'yangilik',
                'verbose_name_plural': 'yangilikar',
            },
        ),
        migrations.CreateModel(
            name='PageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartnerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('image', models.ImageField(upload_to='common/partner/%Y/$m/')),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'partner',
                'verbose_name_plural': 'partners',
            },
        ),
        migrations.CreateModel(
            name='PaymentCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('amount', models.PositiveBigIntegerField(verbose_name='miqdori')),
                ('payment_system', models.CharField(choices=[(1, 'payme'), (2, 'click'), (3, 'paylov'), (4, 'uzumbank')], max_length=255, verbose_name="to'lov tizimi")),
                ('payment_id', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'check',
                'verbose_name_plural': 'checks',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='QuoteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('author', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_en', models.TextField(null=True)),
                ('content_uz', models.TextField(null=True)),
                ('content_ru', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'quote',
                'verbose_name_plural': 'quotes',
            },
        ),
        migrations.CreateModel(
            name='SettingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('email', models.EmailField(max_length=254)),
                ('links', models.URLField()),
                ('appstore_link', models.URLField(blank=True, null=True)),
                ('playmarket_link', models.URLField(blank=True, null=True)),
                ('contact_phone', models.CharField(max_length=13)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('location_text', models.TextField()),
                ('location_text_en', models.TextField(null=True)),
                ('location_text_uz', models.TextField(null=True)),
                ('location_text_ru', models.TextField(null=True)),
                ('telegram', models.CharField(blank=True, max_length=66, null=True)),
                ('instagram', models.CharField(blank=True, max_length=66, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=66, null=True)),
                ('facebook', models.CharField(blank=True, max_length=66, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserContactAppModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('source', models.CharField(choices=[(1, 'mobile'), ('landing', 2)], max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('message', models.TextField(max_length=500, verbose_name='xabar')),
                ('file', models.FileField(blank=True, null=True, upload_to='user-contact/Y%/m%/')),
                ('is_contacted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'User Contact Application',
                'verbose_name_plural': 'User Contact Applications',
                'ordering': ['is_contacted', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='NewsViewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('visitor_id', models.UUIDField(db_index=True)),
                ('ip', models.GenericIPAddressField(db_index=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='common.newmodel')),
            ],
            options={
                'verbose_name': "ko'rilgan yangilik",
                'verbose_name_plural': "ko'rilgan yangiliklar",
            },
        ),
    ]
