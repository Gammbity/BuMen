from modeltranslation.translator import TranslationOptions, register
from course import models

@register(models.VacansyModel)
class VacansyTrans(TranslationOptions):
    fields = ['title', 'company_name', 'description', 'salary']

@register(models.CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(models.StageModel)
class StageTranslationOptions(TranslationOptions):
    fields = ('content',)

@register(models.TestQuestionModel)
class TestQuestionTrans(TranslationOptions):
    fields = ('text',)

@register(models.TestQuestionChoiceModel)
class TestQuetionChoiceTrans(TranslationOptions):
    fields = ['choice']

@register(models.ClubModel)
class ClubTrans(TranslationOptions):
    fields = ['title']