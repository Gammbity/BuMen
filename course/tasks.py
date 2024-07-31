from celery import shared_task
from course import models

@shared_task
def count_lesson_theme_users_count():
    count = 0
    for lesson_theme in models.LessonThemeModel.objects.all():
        lesson_theme.users_count = models.LessonModel.objects.filter(
            lesson__theme=lesson_theme, started_at__isnull=False
        ).count()
        count += 1
        lesson_theme.save()

    return f"{count}: dars mavzulari jarayonda"