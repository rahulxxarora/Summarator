from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .tasks import process

import json


class ProcessData(APIView):
    def get(self, request):

    	returnVal = {}

    	process.delay()

    	returnVal['status']  = True
    	returnVal['message'] = 'Data processing started'

        return Response(json.dumps(returnVal), status.HTTP_200_OK)