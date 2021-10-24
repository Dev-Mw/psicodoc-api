import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import UsersModel
from core.network import HTTPProcess as Http, StatusCode


@method_decorator(csrf_exempt, name='dispatch')
class Users(View):
    """
    API endpoint that allows users to be viewed or edited.
    """
    @staticmethod
    def get(request):
        if request.user.__str__() != 'AnonymousUser':
            if request.user.is_superuser:
                users = [model_to_dict(_, fields=UsersModel.__annotations__.keys())
                         for _ in User.objects.all()]
                return Http.response({'data': users}, StatusCode.OK)
            else:
                user = model_to_dict(User.objects.get(pk=request.user.id),
                                     fields=UsersModel.__annotations__.keys())
                return Http.response(user, StatusCode.OK)
        return Http.response({'message': 'anonymous user'}, StatusCode.OK)

    @staticmethod
    def post(request):
        return JsonResponse({'data': None}, status=200)

    @staticmethod
    def patch(request):
        return JsonResponse({'data': None}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Auth(View):
    """
    API Auth
    """
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        if 'username' in data and 'password' in data:
            user = authenticate(**data)
            if user:
                login(request, user)
                _ = model_to_dict(user, fields=UsersModel.__annotations__.keys())
                return Http.response(_, StatusCode.OK)

        return Http.response({'message': 'invalid credentials'}, StatusCode.OK)

    @staticmethod
    def patch(request):
        logout(request)
        return Http.response({'message': 'ok'}, StatusCode.OK)
