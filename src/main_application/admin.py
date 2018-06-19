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
    fieldsets = (
        (None, {
            'fields': (('file', 'status',), ('display_file_exist', 'display_file_name', 'create_time',), 'change_time',)
        }),
    )

    list_display = ('id', 'display_file_name', 'display_file_exist', 'create_time', 'status', 'change_time')

    readonly_fields = ('create_time', 'file_name', 'display_file_exist', 'display_file_name')

    inlines = [
        FileContentInline
    ]

    def display_file_name(self, obj):
        return obj.file_name

    def display_file_exist(self, obj):
        return obj.file_exist

    display_file_name.short_description = 'File name'

    display_file_exist.boolean = True
    display_file_exist.short_description = 'File exist'
