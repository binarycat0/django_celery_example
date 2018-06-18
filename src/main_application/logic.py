import logging
from time import sleep

from django.core import exceptions

from main_application import models

logger = logging.getLogger(__name__)


def load_content_from_file(some_file_id, speed=None):
    if speed > 1 or speed < 0:
        raise exceptions.ValidationError("Delay is incorrect. Use value [0,1]")

    file_obj = models.SomeFile.objects.get(id=some_file_id)
    if not file_obj:
        raise exceptions.ValidationError("Can't find SomeFile obj by id= %s" % (some_file_id,))

    def _sleep():
        if speed:
            sleep(speed)

    content = models.FileContent.objects.create(file=file_obj)

    with open(file_obj.file_name, 'r') as f:
        for line in f:
            content.append_string(line)
            _sleep()
