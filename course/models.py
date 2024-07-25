from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from user.models import UserModel
from ckeditor.fields import RichTextField

class CategoryModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('nomi'))
    clicked_user = models.ManyToManyField(UserModel, verbose_name=_("tashrif buyurgan foydalanuvchilar"))
    click_count = models.PositiveBigIntegerField(default=0, verbose_name=_("bosish soni"))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

class VacansyModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("sarlavha"))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='lesson-theme', verbose_name=_("kategoriya"))
    company_name = models.CharField(max_length=255, verbose_name=_("kompaniya nomi"))
    description = RichTextField(verbose_name=_("tavsif"))
    salary = models.CharField(max_length=255, verbose_name=_("maosh"))

    class Meta:
        verbose_name = _('vacansy')
        verbose_name_plural = _('vacancies')

class LessonThemeModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("sarlavha"))
    photo = models.FileField(upload_to='lessont-theme/Y%/m%/', verbose_name=_('rasm'))  
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='lesson-theme', verbose_name=_("kategoriya"))

    class Meta:
        verbose_name = _('lesson theme')
        verbose_name_plural = _('lesson themes')

class ClubModel(BaseModel):
    theme = models.ForeignKey(LessonThemeModel, on_delete=models.CASCADE, related_name='club', verbose_name=_("mavzu"))
    title = models.CharField(max_length=255, verbose_name=_("sarlavha"))

    class Meta:
        verbose_name = _('club')
        verbose_name_plural = _('clubs')

class ClubPostModel(BaseModel):
    club = models.ForeignKey(ClubModel, on_delete=models.CASCADE, related_name='club-post', verbose_name=_("klub"))
    content = RichTextField(verbose_name=_("mazmuni"))

    class Meta:
        verbose_name = _('club post')
        verbose_name_plural = _('club posts')

class LessonModel(BaseModel):
    choices = {
        (1, _("mahalliy")),
        (2, _('umumjahon'))
    }
    type = models.Choices(choices, verbose_name=_("turi"))
    theme = models.ForeignKey(LessonThemeModel, on_delete=models.CASCADE, related_name='lesson', verbose_name=_("mavzu"))

    class Meta:
        verbose_name = _('lesson')
        verbose_name_plural = _('lessons')

class StageModel(BaseModel):
    lesson = models.ForeignKey(LessonModel, verbose_name=_("darslik"), on_delete=models.CASCADE)
    content = RichTextField(verbose_name=_("mazmun")) 
    order = models.PositiveIntegerField(verbose_name=_("tartib"))

    class Meta:
        verbose_name = _('stage')
        verbose_name_plural = _('stages')

class StageFileModel(BaseModel):
    file = models.FileField(upload_to='stage_file/Y%/m%/', verbose_name=_("fayl"))
    stage = models.ForeignKey(StageModel, on_delete=models.CASCADE, verbose_name=_("bosqich"))

    class Meta:
        verbose_name = _('stage file')
        verbose_name_plural = _('stage files')

class StageVideoModel(BaseModel):
    video = models.FileField(upload_to='stage_video/Y%/m%/', verbose_name=_("vidyo"))
    stage = models.ForeignKey(StageModel, on_delete=models.CASCADE, verbose_name=_("bosqich"))

    class Meta:
        verbose_name = _('stage video')
        verbose_name_plural = _('stage videos')

class TestQuestionModel(BaseModel):
    stage = models.ForeignKey(StageModel, related_name='test-question', on_delete=models.CASCADE, verbose_name=_("bosqich"))
    text = models.TextField()

    class Meta:
        verbose_name = _('test question')
        verbose_name_plural = _('test questions')
    
class TestQuestionChoiceModel(BaseModel):
    question = models.ForeignKey(TestQuestionModel, related_name='test-question-choice', on_delete=models.CASCADE, verbose_name=_("savol")) 
    text = models.TextField(verbose_name=_("matn"))
    is_correct = models.BooleanField(default=False, verbose_name=_("to'g'riligi"))

    class Meta:
        verbose_name = _('test question choice')
        verbose_name_plural = _('test question choices')

class UserTestAnswer(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_("foydalanuvchi"))
    question = models.ForeignKey(TestQuestionModel, related_name='user-test-answer', on_delete=models.CASCADE, verbose_name=_("savol"))
    answer = models.ForeignKey(TestQuestionChoiceModel, related_name='user-test-answer', on_delete=models.CASCADE, verbose_name=_("javob")) 

    class Meta:
        verbose_name = _('user test answer')
        verbose_name_plural = _('user test answers')

class UserTestResultModel(BaseModel):
    stage = models.ForeignKey(StageModel, verbose_name=_("bosqich"), on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_("foydalanuvchi"))
    question_count = models.PositiveIntegerField(verbose_name=_("savol soni"))
    correct_answers_count = models.PositiveIntegerField(verbose_name=_("to'g'ri javob soni"))
    correct_percent = models.FloatField(verbose_name=_("to'g'rilik foizi"))
    started_at = models.DateTimeField(verbose_name=_("boshlanish vaqti"))
    finished_at = models.DateTimeField(verbose_name=_("tugash vaqti"))

    class Meta:
        verbose_name = _('user test result')
        verbose_name_plural = _('user test results')
