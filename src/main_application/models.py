import logging
from pathlib import Path

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

    @property
    def file_exist(self):
        return Path(self.file.path).exists() if self.file else False

    @property
    def file_name(self):
        return self.file.path if self.file else ''


class FileContent(models.Model):
    id = fields.AutoField(primary_key=True)

    create_time = fields.DateTimeField(default=timezone.now)
    file = models.ForeignKey(SomeFile, on_delete=models.CASCADE, blank=True, null=True)

    content = fields.TextField(blank=True, default="")

    def append_string(self, string: str):
        self.content += ('\n' + string.strip())
        self.save()
