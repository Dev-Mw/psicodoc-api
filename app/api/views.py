from curses.ascii import US
import json
import functools
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import UsersModel, Student, DailyFeeling, UserTest
from core.network import HTTPProcess as Http, StatusCode


@method_decorator(csrf_exempt, name='dispatch')
class Users(View):
    """
    API endpoint that allows users to be viewed or edited.
    """
    @staticmethod
    def get_old(request):
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
        try:
            data = json.loads(request.body)
            username = data["username"]
            email = data["email"]
            password = make_password(data["password"])
            age = data["age"]
            career = data["career"]
            
            if Student.objects.filter(email=email):
                raise ValueError('user already exists')
            student = Student(username=username, email=email, password=password, age=age, career=career)
            student.save()
            return JsonResponse({'data': 'ok'}, status=200)
        except ValueError as e:
            return JsonResponse({'data': 'bad'}, status=400)

    @staticmethod
    def patch(request):
        return JsonResponse({'data': None}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Feeling(View):
    """
    Feeling service
    """
    @staticmethod
    def post(request):
        print(json.loads(request.body))
        try:
            data = json.loads(request.body)
            email = data["email"]
            username = data["username"]
            feeling = data["feeling"]
            student = Student.objects.filter(email=email)
            if len(student) > 0:
                DailyFeeling(email=email,
                             username=username,
                             feeling=feeling,
                             datetimes=datetime.datetime.now().__str__()).save()
                return JsonResponse({'data': 'ok', 'email': student[0].email, 'username': student[0].username}, status=200)
            else:
                return JsonResponse({'data': 'noexists'}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'data': 'bad'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class Auth(View):
    """
    API Auth service
    """
    @staticmethod
    def post(request):
        try:
            data = json.loads(request.body)
            email = str(data["email"]).strip()
            password = str(data["password"]).strip()
            student = Student.objects.filter(email=email)
            if len(student) > 0:
                if check_password(password, student[0].password):
                    return JsonResponse({'data': 'ok', 'email': student[0].email, 'username': student[0].username}, status=200)
                else:
                    return JsonResponse({'data': 'badcred'}, status=400)
            else:
                return JsonResponse({'data': 'noexists'}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'data': 'bad'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class UserTests(View):
    """
    API Auth service
    """
    @staticmethod
    def post(request):
        try:
            data = json.loads(request.body)
            email = str(data["email"]).strip()
            test = data["test"]
            student = Student.objects.filter(email=email)
            if len(student) > 0:
                times = datetime.datetime.now().__str__()
                res = {
                    "email": student[0].email,
                    "username": student[0].username,
                    "datetimes": times,
                }
                i = 1
                for k, v in test.items():
                    res[f"question{i}"] = k
                    res[f"answer{i}"] = v
                    i += 1
                UserTest(**res).save()
                return JsonResponse({'data': 'ok', 'email': student[0].email, 'username': student[0].username}, status=200)
            else:
                return JsonResponse({'data': 'noexists'}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'data': 'bad'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class FeelingHistory(View):
    """
    List feeling history
    """
    @staticmethod
    def post(request):
        try:
            data = json.loads(request.body)
            email = str(data["email"]).strip()
            student = Student.objects.filter(email=email)
            if len(student) > 0:
                list_feeling = {}
                feeling_history = DailyFeeling.objects.filter(email=email)
                for f in feeling_history:
                    if f.feeling in list_feeling:
                        list_feeling[f.feeling] = list_feeling[f.feeling] + 1
                    else:
                        list_feeling[f.feeling] = 1
                
                total_count = functools.reduce(lambda x, y: x + y, list_feeling.values())
                
                for k, v in list_feeling.items():
                    list_feeling[k] = "%.1f" % (100 * v / total_count)
                    
                print(list_feeling)
        
                return JsonResponse({'data': 'ok', 'email': student[0].email, 'total': list_feeling}, status=200)
            else:
                return JsonResponse({'data': 'noexists'}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'data': 'bad'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class _Auth(View):
    """
    API Auth service
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
