from django.db import models

# Create your models here.
from django.db.models import fields


class ObjectWithFile(models.Model):
    id = fields.AutoField(primary_key=True)

    # file will be uploaded to MEDIA_ROOT/uploads
    file = models.FileField(upload_to='upload/', blank=True, null=True)
    status = fields.CharField(max_length=15, default='new', choices=(('new', 'new'), ('processed', 'processed')))

    file_name = fields.CharField(max_length=249, default='', blank=True)

    def save(self, *args, **kwargs):
        self.file_name = self.file.path if self.file else '_blank_'
        super().save(*args, **kwargs)
