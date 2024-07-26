from django.apps import AppConfig


class CourseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course'

    def ready(self) -> None:
        from course.signals import create_local_and_international_lessons