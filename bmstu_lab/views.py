from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Autors, Articles, Subjects
from .serializers import ArticleSerializer, SubjectSerializer, AutorSerializer
### PART FROM VIDEO
### PART FROM VIDEO
### PART FROM VIDEO
from django.db import models
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.first_name

@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        print("WE ARE HERE")
        data = self.request.data
        username = data['username']
        password = data['password']
        re_password  = data['re_password']
        try:
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return Response({ 'error': 'Username already exists' })
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user = User.objects.get(id=user.id)
                    return Response({ 'success': 'User created successfully' })
            else:
                return Response({ 'error': 'Passwords do not match' })
        except Exception as e:
                return Response({ 'error': 'Something went wrong when registering account' })

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):  # Get our csrf cookie in application
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
        return Response({ 'success': 'CSRF cookie set' })

def GetArticles(request):
    subjects = Subjects.objects.all()
    return render(request, 'bmstu_lab/topics.html', {'data' : subjects})

def GetArticle(request, id):
    articles_by_group = Articles.objects.filter(subject_id=id)
    return render(request, 'bmstu_lab/articles.html', {'data' :  articles_by_group})


class AutorsViewSet(viewsets.ModelViewSet):
    queryset = Autors.objects.all()
    serializer_class = AutorSerializer

class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

class ArticlesViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()

    def get_queryset(self):
        queryset = Articles.objects.all()
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        text = self.request.query_params.get("text")
        if min_price is not None and max_price is not None and text is not None:
            filtered_queryset = []
            for query in queryset:
                if query.price >= int(min_price) and \
                        query.price <= int(max_price) and \
                        (text == "" or text.lower() in query.title.lower()):
                    filtered_queryset.append(query)
            return filtered_queryset
        return queryset
