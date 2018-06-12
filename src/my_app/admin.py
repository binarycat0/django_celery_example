from django.contrib import admin

# Register your models here.
from my_app import models


@admin.register(models.MyModel)
class MyClassAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'create_date', 'change_time', 'text', 'random_text',)
    readonly_fields = ('pk',)

    fieldsets = (
        (
            None, {
                'fields': (
                    'pk', 'status',
                    ('create_date', 'change_time',),
                    'text', 'random_text',
                )
            }
        ),
    )
