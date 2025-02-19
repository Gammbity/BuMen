import os
from celery.schedules import crontab
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('bumen')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "news_views_cleaner": {
        "task": "common.tasks.news_views_cleaner",
        "schedule": crontab(hour='15', minute='1')
    },
    "count_lesson_theme_users_count": {
        "task": "course.tasks.count_lesson_theme_users_count",
        "schedule": crontab(minute='*/1')
    }
}