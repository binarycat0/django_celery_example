import logging

from main_application import logic
from main_application.celery import app

logger = logging.getLogger(__name__)


@app.task(bind=True)
def load_content_from_file(self, some_file_id, delay=None):
    try:
        logger.info('START _ load_content_from_file')
        logic.load_content_from_file(some_file_id, delay)
    except Exception as ex:
        logger.info('EXCEPTION _ load_content_from_file')
        logger.exception(ex)
        raise ex

    return True
