# Generated by Django 5.0.6 on 2024-07-28 12:33

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('name', models.CharField(max_length=255, verbose_name='nomi')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='nomi')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='nomi')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='nomi')),
                ('click_count', models.PositiveBigIntegerField(default=0, verbose_name='bosish soni')),
            ],
            options={
                'verbose_name': 'kategoriy',
                'verbose_name_plural': 'kategoriyalar',
                'ordering': ['-click_count'],
            },
        ),
        migrations.CreateModel(
            name='ClubModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('title', models.CharField(max_length=255, verbose_name='sarlavha')),
            ],
            options={
                'verbose_name': 'klub',
                'verbose_name_plural': 'klublar',
            },
        ),
        migrations.CreateModel(
            name='ClubPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('content', ckeditor.fields.RichTextField(verbose_name='mazmuni')),
            ],
            options={
                'verbose_name': 'klub kantenti',
                'verbose_name_plural': 'klub kantentlari',
            },
        ),
        migrations.CreateModel(
            name='DicussionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('text', models.TextField(verbose_name='matn')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='discussion-photo/%Y/%m/', verbose_name='rasm')),
                ('file', models.FileField(blank=True, null=True, upload_to='discussion-file/%Y/%m/', verbose_name='fayl')),
            ],
            options={
                'verbose_name': 'muhokama',
                'verbose_name_plural': 'muhokamalar',
            },
        ),
        migrations.CreateModel(
            name='DiscussionCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('text', models.TextField(verbose_name='matn')),
            ],
            options={
                'verbose_name': 'muhokama izohi',
                'verbose_name_plural': 'muhokama izohlari',
            },
        ),
        migrations.CreateModel(
            name='LessonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('type', models.CharField(choices=[(1, 'mahalliy'), (2, 'umumjahon')], max_length=100, verbose_name='turi')),
            ],
            options={
                'verbose_name': 'darslik',
                'verbose_name_plural': 'darsliklar',
            },
        ),
        migrations.CreateModel(
            name='LessonThemeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('title', models.CharField(max_length=255, verbose_name='sarlavha')),
                ('photo', models.ImageField(upload_to='lessont-theme/%Y/%m/', verbose_name='rasm')),
                ('author', models.CharField(max_length=255, verbose_name='avtor')),
            ],
            options={
                'verbose_name': 'dars mavzusi',
                'verbose_name_plural': 'dars mavzulari',
            },
        ),
        migrations.CreateModel(
            name='StageFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('file', models.FileField(upload_to='stage_file/%Y/%m/', verbose_name='fayl')),
            ],
            options={
                'verbose_name': 'bosqich fayli',
                'verbose_name_plural': 'bosqich fayllari',
            },
        ),
        migrations.CreateModel(
            name='StageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='mazmun')),
                ('order', models.PositiveIntegerField(verbose_name='tartib')),
            ],
            options={
                'verbose_name': 'bosqich',
                'verbose_name_plural': 'bosqichlar',
            },
        ),
        migrations.CreateModel(
            name='StageVideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('video', models.FileField(upload_to='stage_video/%Y/%m/', verbose_name='vidyo')),
            ],
            options={
                'verbose_name': 'bosqich vidyosi',
                'verbose_name_plural': 'bosqich vidyolari',
            },
        ),
        migrations.CreateModel(
            name='TestQuestionChoiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('text', models.TextField(verbose_name='matn')),
                ('is_correct', models.BooleanField(default=False, verbose_name="to'g'riligi")),
            ],
            options={
                'verbose_name': 'test savol varianti',
                'verbose_name_plural': 'test savol variantlari',
            },
        ),
        migrations.CreateModel(
            name='TestQuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('text', models.TextField(verbose_name='matn')),
            ],
            options={
                'verbose_name': 'test savoli',
                'verbose_name_plural': 'test savollari',
            },
        ),
        migrations.CreateModel(
            name='UserLessonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('last_seen_at', models.DateTimeField(verbose_name="so'nggi ko'rilgan")),
            ],
            options={
                'verbose_name': 'foydalanvchi darsligi',
                'verbose_name_plural': 'foydalanvchi darsliklari',
                'ordering': ['-last_seen_at'],
            },
        ),
        migrations.CreateModel(
            name='UserTestAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
            ],
            options={
                'verbose_name': 'foydalanvchi test javobi',
                'verbose_name_plural': 'foydalanvchi test javoblari',
            },
        ),
        migrations.CreateModel(
            name='UserTestResultModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('question_count', models.PositiveIntegerField(verbose_name='savol soni')),
                ('correct_answers_count', models.PositiveIntegerField(verbose_name="to'g'ri javob soni")),
                ('correct_percent', models.PositiveIntegerField(verbose_name="to'g'rilik foizi")),
                ('started_at', models.DateTimeField(verbose_name='boshlanish vaqti')),
                ('finished_at', models.DateTimeField(verbose_name='tugash vaqti')),
            ],
            options={
                'verbose_name': 'foydalanvchi test natijasi',
                'verbose_name_plural': 'foydalanvchi test natijalari',
            },
        ),
        migrations.CreateModel(
            name='VacansyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqti')),
                ('title', models.CharField(max_length=255, verbose_name='sarlavha')),
                ('company_name', models.CharField(max_length=255, verbose_name='kompaniya_nomi')),
                ('description', ckeditor.fields.RichTextField(verbose_name='tavsif')),
                ('salary', models.CharField(max_length=255, verbose_name='maosh')),
            ],
            options={
                'verbose_name': "bo'sh ish o'rni",
                'verbose_name_plural': "bo'sh ish o'rinlari",
            },
        ),
    ]
