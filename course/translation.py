from modeltranslation.translator import TranslationOptions, register
from course import models

@register(models.CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
