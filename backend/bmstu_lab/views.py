from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Autors, Articles, Subjects
from .serializers import ArticleSerializer, SubjectSerializer, AutorSerializer, UserSerializer
### PART FROM VIDEO
### PART FROM VIDEO
### PART FROM VIDEO
from django.db import models
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.views.decorators.csrf import csrf_exempt


class GetUserProfileView(APIView):
    def get(self, request, format=None):
        # try:
        user = self.request.user
        username = user.username
        print(username)
        print(user)

        user_profile = UserProfile.objects.get(user=user)
        user_profile = UserProfileSerializer(user_profile)

        return Response({ 'profile': user_profile.data, 'username': str(username) })
        # except:
        #     return Response({ 'error': 'Something went wrong when retrieving profile' })


class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        print('STARTED')
        user = self.request.user
        print(user)
        try:
            isAuthenticated = user.is_authenticated
            if isAuthenticated:
                return Response({'isAuthenticated': 'success'})
            else:
                return Response({'isAuthenticated': 'error'})
        except Exception as e:
            print(e)
            return Response({'error': 'Something went wrong when checking authentication status'})


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        print("WE ARE HERE")
        data = self.request.data
        username = data['username']
        password = data['password']
        re_password = data['re_password']
        try:
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return Response({'error': 'Username already exists'})
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user = User.objects.get(id=user.id)
                    user_profile = UserProfile.objects.create(user=user, first_name='', last_name='', phone='', city='')
                    return Response({'success': 'User created successfully'})
            else:
                return Response({'error': 'Passwords do not match'})
        except Exception as e:
            return Response({'error': 'Something went wrong when registering account'})


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        username = data['username']
        password = data['password']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return Response({'success': 'User authenticated',
                                 'username': username})
            else:
                return Response({'error': 'Error Authenticating'})
        except:
            return Response({'error': 'Something went wrong when logging in'})


class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success': 'Loggout Out'})
        except:
            return Response({'error': 'Something went wrong when logging out'})


class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user
        try:
            User.objects.filter(id=user.id).delete()
            return Response({'success': 'User deleted successfully'})
        except:
            return Response({'error': 'Something went wrong when trying to delete user'})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):  # Get our csrf cookie in application
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})


def GetArticles(request):
    permission_classes = (permissions.AllowAny,)
    subjects = Subjects.objects.all()
    return render(request, 'bmstu_lab/topics.html', {'data': subjects})


def GetArticle(request, id):
    permission_classes = (permissions.AllowAny,)
    articles_by_group = Articles.objects.filter(subject_id=id)
    return render(request, 'bmstu_lab/articles.html', {'data': articles_by_group})


class AutorsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Autors.objects.all()
    serializer_class = AutorSerializer


class SubjectsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

class ArticlesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
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


class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data)
