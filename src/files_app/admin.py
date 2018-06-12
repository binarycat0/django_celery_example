from django.contrib import admin

# Register your models here.
from files_app import models


@admin.register(models.ObjectWithFile)
class ObjectWithFileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'file_name', 'file', 'status')
