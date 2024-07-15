from modeltranslation.translator import register, TranslationOptions
from common import models

@register(models.SettingsModel)
class SettingTrans(TranslationOptions):
    fields = ['location_text']

@register(models.AboutAppModel)
class AboutAppTrans(TranslationOptions):
    fields = ['caption', 'text']

@register(models.FAQModel)
class FAQTrans(TranslationOptions):
    fields = ['question', 'answer']

@register(models.QuoteModel)
class QuoteTrans(TranslationOptions):
    fields = ['content']


@register(models.PageModel)
class PageTrans(TranslationOptions):
    fields = ['title', 'content']