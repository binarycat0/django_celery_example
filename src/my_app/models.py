import datetime
import logging

from django.db import models
from django.db.models import fields
from django.db.transaction import atomic

logger = logging.getLogger(__name__)

STATUS = (
    ('new', 'new'),
    ('progress', 'progress'),
    ('done', 'done'),
)


class MyModel(models.Model):
    id = fields.AutoField(primary_key=True)

    status = fields.CharField(max_length=20, blank=False, null=False, default='new', choices=STATUS)

    create_date = fields.DateTimeField(blank=False, null=False, default=datetime.datetime.now)
    change_time = fields.DateTimeField(blank=True, null=True)

    text = fields.CharField(max_length=150, blank=True, null=False, default="")
    random_text = fields.CharField(max_length=150, blank=True, null=False, default="")

    @atomic
    def progress(self):
        self.change_time = datetime.datetime.now()
        self.status = 'progress'
        self.save()
        
    @atomic
    def done(self):
        self.change_time = datetime.datetime.now()
        self.status = 'done'
        self.save()
