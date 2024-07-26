from django.contrib import admin
from django.http import HttpRequest
from modeltranslation.admin import TranslationAdmin
from course import models
from django.utils.safestring import mark_safe

@admin.register(models.CategoryModel)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name']
    search_fields = ['name_uz', 'name_ru', 'name_en']


class LessonInline(admin.TabularInline):
    model = models.LessonModel
    extra = 0
    readonly_fields = ['type']

    def has_delete_permission(self, request: HttpRequest, obj) -> bool:
        return False
    
    def has_add_permission(self, request: HttpRequest, obg=None) -> bool:
        return False
    
    def link(self, instance):
        url = f'admin/course/lesson/{instance.id}/change'
        return mark_safe('<a target="_blank" href="{url}">Kirish</a>')
    
@admin.register(models.LessonThemeModel)
class LessonThemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

    inlines = [LessonInline]


@admin.register(models.LessonModel)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['type', 'theme']
    readonly_fields = ['type', 'theme']
