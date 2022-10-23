from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Autors, Articles, Subjects
from .serializers import ArticleSerializer, SubjectSerializer, AutorSerializer

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
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

# class SubjectAPIView(generics.ListCreateAPIView):
#     queryset = Subjects.objects.all()
#     serializer_class = SubjectSerializer
#
# class AutorsAPIView(generics.ListCreateAPIView):
#     queryset = Autors.objects.all()
#     serializer_class = AutorSerializer
#
# class ArticlesAPIView(generics.ListCreateAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticleSerializer
