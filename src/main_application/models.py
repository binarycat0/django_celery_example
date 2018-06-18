import logging

from django.db import models
from django.db.models import fields
from django.utils import timezone

logger = logging.getLogger(__name__)

STATUS = (
    ('new', 'new'),
    ('progress', 'progress'),
    ('done', 'done'),
)


class SomeFile(models.Model):
    id = fields.AutoField(primary_key=True)

    create_time = fields.DateTimeField(default=timezone.now)
    change_time = fields.DateTimeField(blank=True, null=True)

    # file will be uploaded to MEDIA_ROOT/upload
    file = models.FileField(upload_to='upload/', blank=True, null=True)
    status = fields.CharField(
        max_length=20, default='new',
        choices=STATUS
    )

    file_name = fields.CharField(max_length=249, default='', blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.file_name = self.file.path if self.file else '_blank_'
        print(self.create_time)

        super().save(*args, **kwargs)


class FileContent(models.Model):
    id = fields.AutoField(primary_key=True)

    create_time = fields.DateTimeField(default=timezone.now)
    file = models.ForeignKey(SomeFile, on_delete=models.CASCADE, blank=True, null=True)

    content = fields.TextField(blank=True, default="")
