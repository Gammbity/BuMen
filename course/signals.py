from django.dispatch import receiver
from course import models
from django.db.models.signals import post_save


@receiver(post_save, sender=models.LessonThemeModel)
def create_local_and_international_lessons(sender, instance, created, **kwargs):
    if created:
        choices = models.LessonModel.choices
        local = choices[0][1]
        inter = choices[1][1]
        models.LessonModel.objects.create(
            theme=instance,
            type = 1
        ) 
        models.LessonModel.objects.create(
            theme=instance,
            type = 2
        )    