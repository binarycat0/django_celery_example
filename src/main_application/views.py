import logging

from django.http import JsonResponse
from django.views import generic

from main_application import tasks

logger = logging.getLogger(__name__)


class Test(generic.DetailView):

    def get(self, request, *args, **kwargs):

        id = request.GET.get('id', None)

        logger.debug("get params: %s", request.GET)

        if id:
            logger.debug("id: %s", id)
            res = tasks.change_status_my_model.delay(model_id=id)
            return JsonResponse(data={'res': res.id})
        else:
            return JsonResponse(data={'id': id})
