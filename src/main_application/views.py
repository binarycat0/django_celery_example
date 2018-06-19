import logging

from django.http import JsonResponse
from django.views import generic

from main_application.utils import random_string

logger = logging.getLogger(__name__)


class Test(generic.DetailView):

    def get(self, request, *args, **kwargs):
        return JsonResponse(data={'ok': 200})


class UploadFile(generic.View):

    def post(self, request, *args, **kwargs):
        logger.info(request.FILES['file'])

        handle_uploaded_file(request.FILES['file'])

        return JsonResponse(data={'ok': 200})


def handle_uploaded_file(f):
    _temp_file_name = '/tmp/' + random_string()
    with open(_temp_file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    logger.info('Upload new file: %s', _temp_file_name)
