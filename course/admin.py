from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationStackedInline
from course import models
from django.utils.safestring import mark_safe
from django.db import models as dj_models
from django.contrib.admin.widgets import AdminTextareaWidget

@admin.register(models.VacansyModel)
class VacansyAdmin(TranslationAdmin):
    list_display = ['title']
    list_display_links = ['title']

@admin.register(models.CategoryModel)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name']
    search_fields = ['name_uz', 'name_ru', 'name_en']


class LessonInline(admin.TabularInline):
    model = models.LessonModel
    extra = 0
    readonly_fields = ['type', 'link', 'id']

    def has_delete_permission(self, request: HttpRequest, obj) -> bool:
        return False
    
    def has_add_permission(self, request: HttpRequest, obg=None) -> bool:
        return False
    
    def link(self, instance):
        url = f'/admin/course/lessonmodel/{instance.id}/change'
        return mark_safe(f'<a target="_blank" href="{url}">Kirish</a>')
    
@admin.register(models.LessonThemeModel)
class LessonThemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    inlines = [LessonInline]


class StageVideoAdmin(admin.TabularInline):
    model = models.StageVideoModel
    extra = 0

class StageFileAdmin(admin.TabularInline):
    model = models.StageFileModel
    extra = 0

class StageInline(TranslationTabularInline):
    model=models.StageModel
    readonly_fields = ['link']
    fields = ['order', 'link']
    extra = 0

    def link(slef, stage):
        url = f'/admin/course/stagemodel/{stage.id}/change/'
        return mark_safe(f'<a target="_blank" href="{url}">Kirish</a>') 

# @admin.register(models.TestQuestionChoiceModel)
# class TestQuestionChoiceInline(admin.ModelAdmin):
#     pass

class TestQuestionChoiceInline(TranslationStackedInline):
    model = models.TestQuestionChoiceModel
    fields = ['is_correct', 'choice']

    form_field = {
        dj_models.TextField: {'widget': AdminTextareaWidget(attrs={'rows': 1, 'col': 80})}
    }

    def get_extra(self, request: HttpRequest, obj: Any | None = ..., **kwargs: Any) -> int:
        if obj:
            choices_count = obj.testquestion_choice.count()
            if choices_count >= 4:
                return 0
            return 4 - choices_count
    
@admin.register(models.TestQuestionModel)
class TestQuestionAdmin(TranslationAdmin):
    readonly_fields = ['stage']
    fields = ['stage', 'text']
    inlines = [TestQuestionChoiceInline]

    def has_module_permission(self, request: HttpRequest) -> bool:
        return False


class TestQuestionInline(admin.TabularInline):
    model = models.TestQuestionModel
    fields = ['text', 'link']
    readonly_fields = ['link']
    extra = 0

    def link(self,instanse):
        url = f"/admin/course/testquestionmodel/{instanse.id}/change/"
        return mark_safe(f'<a terget=_blank href="{url}">Kirish</a>')

@admin.register(models.StageModel)
class StageAdmin(TranslationAdmin):
    list_display = ['content']
    list_display_links = ['content']
    readonly_fields = ['lesson', 'order']
    fields = ('lesson', 'order', 'content')
    inlines = [StageFileAdmin, StageVideoAdmin, TestQuestionInline]

    def has_module_permission(self, request: HttpRequest) -> bool:
        return False

@admin.register(models.LessonModel)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['type', 'theme']
    list_display_links = ['type', 'theme']
    readonly_fields = ['type', 'theme']
    inlines = [StageInline]

    def has_module_permission(self, request: HttpRequest) -> bool:
        return False 

