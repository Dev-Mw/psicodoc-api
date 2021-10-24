from typing import Dict
from django.http.response import JsonResponse


class StatusCode:
    OK = 200
    FORBIDDEN = 403
    BAD_REQUEST = 400
    BAD_GATEWAY = 500


class HTTPProcess(object):
    @staticmethod
    def response(data: Dict, /, code: StatusCode):
        print(code)
        return JsonResponse(data, status=code)
