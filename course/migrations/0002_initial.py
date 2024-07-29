# Generated by Django 5.0.6 on 2024-07-28 12:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='clicked_user',
            field=models.ManyToManyField(related_name='category', to=settings.AUTH_USER_MODEL, verbose_name='tashrif buyurgan foydalanuvchilar'),
        ),
        migrations.AddField(
            model_name='clubpostmodel',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_post', to='course.clubmodel', verbose_name='klub'),
        ),
        migrations.AddField(
            model_name='dicussionmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion', to=settings.AUTH_USER_MODEL, verbose_name='foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='discussioncommentmodel',
            name='discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion_comment', to='course.dicussionmodel', verbose_name='munozara'),
        ),
        migrations.AddField(
            model_name='discussioncommentmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion_comment', to=settings.AUTH_USER_MODEL, verbose_name='foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='dicussionmodel',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion', to='course.lessonmodel', verbose_name='darslik'),
        ),
        migrations.AddField(
            model_name='lessonthememodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_theme', to='course.categorymodel', verbose_name='kategoriya'),
        ),
        migrations.AddField(
            model_name='lessonmodel',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='course.lessonthememodel', verbose_name='mavzu'),
        ),
        migrations.AddField(
            model_name='clubmodel',
            name='theme',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='club', to='course.lessonthememodel', verbose_name='mavzu'),
        ),
        migrations.AddField(
            model_name='stagemodel',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage', to='course.lessonmodel', verbose_name='darslik'),
        ),
        migrations.AddField(
            model_name='stagefilemodel',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.stagemodel', verbose_name='bosqich'),
        ),
        migrations.AddField(
            model_name='stagevideomodel',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.stagemodel', verbose_name='bosqich'),
        ),
        migrations.AddField(
            model_name='testquestionmodel',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_question', to='course.stagemodel', verbose_name='bosqich'),
        ),
        migrations.AddField(
            model_name='testquestionchoicemodel',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testquestion_choice', to='course.testquestionmodel', verbose_name='savol'),
        ),
        migrations.AddField(
            model_name='userlessonmodel',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_lesson_theme', to='course.lessonmodel', verbose_name='darslik'),
        ),
        migrations.AddField(
            model_name='userlessonmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_lesson_theme', to=settings.AUTH_USER_MODEL, verbose_name='foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='usertestanswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_test_answer', to='course.testquestionchoicemodel', verbose_name='javob'),
        ),
        migrations.AddField(
            model_name='usertestanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_test_answer', to='course.testquestionmodel', verbose_name='savol'),
        ),
        migrations.AddField(
            model_name='usertestanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='usertestresultmodel',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.stagemodel', verbose_name='bosqich'),
        ),
        migrations.AddField(
            model_name='usertestresultmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='vacansymodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacansy', to='course.categorymodel', verbose_name='kategoriya'),
        ),
        migrations.AlterUniqueTogether(
            name='lessonmodel',
            unique_together={('theme', 'type')},
        ),
        migrations.AlterUniqueTogether(
            name='userlessonmodel',
            unique_together={('user', 'lesson')},
        ),
    ]
