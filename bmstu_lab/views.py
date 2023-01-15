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
