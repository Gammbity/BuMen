from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from user.models import UserModel
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class CategoryModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('nomi'))
    clicked_user = models.ManyToManyField(UserModel, verbose_name=_("tashrif buyurgan foydalanuvchilar"), related_name="category")
    click_count = models.PositiveBigIntegerField(default=0, verbose_name=_("bosish soni"))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-click_count']
        verbose_name = _('kategoriy')
        verbose_name_plural = _('kategoriyalar')

class VacansyModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("sarlavha"))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='vacansy', verbose_name=_("kategoriya"))
    company_name = models.CharField(max_length=255, verbose_name=_("kompaniya_nomi"))
    description = RichTextField(verbose_name=_("tavsif"))
    salary = models.CharField(max_length=255, verbose_name=_("maosh"))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _("bo'sh ish o'rni")
        verbose_name_plural = _("bo'sh ish o'rinlari")

class LessonThemeModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("sarlavha"))
    photo = models.ImageField(upload_to='lessont-theme/%Y/%m/', verbose_name=_('rasm')) 
    author = models.CharField(max_length=255, verbose_name=_('avtor')) 
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='lesson_theme', verbose_name=_("kategoriya"))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('dars mavzusi')
        verbose_name_plural = _('dars mavzulari')

class ClubModel(BaseModel):
    theme = models.OneToOneField(LessonThemeModel, on_delete=models.CASCADE, related_name='club', verbose_name=_("mavzu"))
    title = models.CharField(max_length=255, verbose_name=_("sarlavha"))

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('klub')
        verbose_name_plural = _('klublar')

class ClubPostModel(BaseModel):
    club = models.ForeignKey(ClubModel, on_delete=models.CASCADE, related_name='club_post', verbose_name=_("klub"))
    content = RichTextField(verbose_name=_("mazmuni"))

    class Meta:
        verbose_name = _('klub kantenti')
        verbose_name_plural = _('klub kantentlari')

class LessonModel(BaseModel):
    choices = (
        (1, _("mahalliy")),
        (2, _('umumjahon'))
    )
    type = models.IntegerField(choices=choices, verbose_name=_("turi"))
    theme = models.ForeignKey(LessonThemeModel, on_delete=models.CASCADE, related_name='lesson', verbose_name=_("mavzu"))

    def __str__(self) -> str:
        return f"{self.theme} | {self.type}"

    class Meta:
        unique_together = ['theme', 'type']
        verbose_name = _('darslik')
        verbose_name_plural = _('darsliklar')
        
class DicussionModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_("foydalanuvchi"), related_name="discussion")
    lesson = models.ForeignKey(LessonModel, verbose_name=_("darslik"), on_delete=models.CASCADE, related_name="discussion")
    text = models.TextField(verbose_name=_("matn"))
    photo = models.ImageField(upload_to="discussion-photo/%Y/%m/", null=True, blank=True, verbose_name=_("rasm"))
    file = models.FileField(upload_to="discussion-file/%Y/%m/", null=True, blank=True, verbose_name=_("fayl"))

    class Meta:
        verbose_name = _('muhokama')
        verbose_name_plural = _('muhokamalar')

class DiscussionCommentModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_("foydalanuvchi"), related_name="discussion_comment")
    discussion = models.ForeignKey(DicussionModel, on_delete=models.CASCADE, verbose_name=_("munozara"), related_name="discussion_comment")
    text = models.TextField(verbose_name=_("matn"))

    class Meta:
        verbose_name = _('muhokama izohi')
        verbose_name_plural = _('muhokama izohlari')

class StageModel(BaseModel):
    lesson = models.ForeignKey(LessonModel, verbose_name=_("darslik"), on_delete=models.CASCADE, related_name="stage")
    content = RichTextUploadingField(verbose_name=_("mazmun")) 
    order = models.PositiveIntegerField(verbose_name=_("tartib"))

    def __str__(self) -> str:
        return f'{self.lesson} | {self.order} - bosqich'
    
    class Meta:
        verbose_name = _('bosqich')
        verbose_name_plural = _('bosqichlar')

class StageFileModel(BaseModel):
    file = models.FileField(upload_to='stage_file/%Y/%m/', verbose_name=_("fayl"))
    stage = models.ForeignKey(StageModel, on_delete=models.CASCADE, verbose_name=_("bosqich"))

    class Meta:
        verbose_name = _('bosqich fayli')
        verbose_name_plural = _('bosqich fayllari')

class StageVideoModel(BaseModel):
    video = models.FileField(upload_to='stage_video/%Y/%m/', verbose_name=_("vidyo"))
    stage = models.ForeignKey(StageModel, on_delete=models.CASCADE, verbose_name=_("bosqich"))

    class Meta:
        verbose_name = _('bosqich vidyosi')
        verbose_name_plural = _('bosqich vidyolari')

class TestQuestionModel(BaseModel):
    stage = models.ForeignKey(StageModel, related_name='test_question', on_delete=models.CASCADE, verbose_name=_("bosqich"))
    text = models.TextField(verbose_name=_("matn"))

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = _('test savoli')
        verbose_name_plural = _('test savollari')
    
class TestQuestionChoiceModel(BaseModel):
    question = models.ForeignKey(TestQuestionModel, related_name='testquestion_choice', on_delete=models.CASCADE, verbose_name=_("savol")) 
    choice = models.TextField(verbose_name=_("matn"))
    is_correct = models.BooleanField(default=False, verbose_name=_("to'g'riligi"))

    def __str__(self) -> str:
        return self.choice
    
    class Meta:
        verbose_name = _('test savol varianti')
        verbose_name_plural = _('test savol variantlari')

class UserTestAnswer(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_("foydalanuvchi"))
    question = models.ForeignKey(TestQuestionModel, related_name='user_test_answer', on_delete=models.CASCADE, verbose_name=_("savol"))
    answer = models.ForeignKey(TestQuestionChoiceModel, related_name='user_test_answer', on_delete=models.CASCADE, verbose_name=_("javob")) 

    class Meta:
        verbose_name = _('foydalanvchi test javobi')
        verbose_name_plural = _('foydalanvchi test javoblari')

class UserTestResultModel(BaseModel):
    stage = models.ForeignKey(StageModel, verbose_name=_("bosqich"), on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_("foydalanuvchi"))
    question_count = models.PositiveIntegerField(verbose_name=_("savol soni"))
    correct_answers_count = models.PositiveIntegerField(verbose_name=_("to'g'ri javob soni"))
    correct_percent = models.PositiveIntegerField(verbose_name=_("to'g'rilik foizi"))
    started_at = models.DateTimeField(verbose_name=_("boshlanish vaqti"))
    finished_at = models.DateTimeField(verbose_name=_("tugash vaqti"))

    class Meta:
        verbose_name = _('foydalanvchi test natijasi')
        verbose_name_plural = _('foydalanvchi test natijalari')

class UserLessonModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="user_lesson_theme", verbose_name=_('foydalanuvchi'))
    lesson = models.ForeignKey(LessonModel, on_delete=models.CASCADE, related_name="user_lesson_theme", verbose_name=_("darslik"))
    last_seen_at = models.DateTimeField(verbose_name=_("so'nggi ko'rilgan"))

    class Meta:
        unique_together = ['user', 'lesson']
        ordering = ['-last_seen_at']
        verbose_name = _('foydalanvchi darsligi')
        verbose_name_plural = _('foydalanvchi darsliklari')