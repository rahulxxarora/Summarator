from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .tasks import scrape

import json


class Scrape(APIView):
    def get(self, request, scraper):

    	returnVal = {}

        scrape.delay(scraper)

    	returnVal['status']  = True
    	returnVal['message'] = 'Scraper started successfully'

        return Response(json.dumps(returnVal), status.HTTP_200_OK)