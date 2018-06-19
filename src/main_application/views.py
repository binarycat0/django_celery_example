import logging

from django.http import JsonResponse
from django.views import generic

logger = logging.getLogger(__name__)


class Test(generic.DetailView):

    def get(self, request, *args, **kwargs):
        return JsonResponse(data={'ok': 200})
