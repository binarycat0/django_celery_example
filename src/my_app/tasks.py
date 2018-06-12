import logging

from my_app import models
from my_app.celery import app

logger = logging.getLogger(__name__)


@app.task(bind=True)
def change_status_my_model(*args, **kwargs):
    logger.debug('kwargs %s', str(kwargs))

    model_id = kwargs.get('model_id', None)
    logger.debug('model_id %s', model_id)

    logger.debug(str(models.MyModel.objects.all()))

    obj = models.MyModel.objects.filter(pk=int(model_id)).first()
    if obj:
        obj.progress()
        return obj.status

    return 'fail'
