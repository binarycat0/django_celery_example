from django.contrib import admin

# Register your models here.
from main_application import models


@admin.register(models.FileContent)
class FileContentAdmin(admin.ModelAdmin):
    pass


class FileContentInline(admin.TabularInline):
    model = models.FileContent
    fk_name = 'file'
    extra = 1
    fields = ('id', 'create_time',)
    show_change_link = True
    readonly_fields = ('id', 'create_time',)


@admin.register(models.SomeFile)
class SomeFileAdmin(admin.ModelAdmin):
    inlines = [
        FileContentInline
    ]
