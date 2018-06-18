from django.contrib import admin

# Register your models here.
from main_application import models


@admin.register(models.FileContent)
class FileContentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SomeFile)
class SomeFileAdmin(admin.ModelAdmin):
    pass
