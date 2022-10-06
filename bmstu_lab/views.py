from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
# View in django, controller in MVC
class Data: # класс с данными (замена БД)
    def __init__(self):
        self.titles = [
            {'title': 'Physics', 'id': 1},
            {'title': 'Mathematics', 'id': 2},
            {'title': 'Artificial intellegence', 'id': 3},
        ]
        ids_category = [1, 2, 3]
        self.articles_for_category = [["Physics mechanics"],
                                 ["Linear algebra"],
                                 ["CNN for detection", "Future AI"]]
        self.images_for_category = [["imgs/physics1.jpg"],
                               ["imgs/math1.jpg"],
                               ["imgs/nn1.jpg", "imgs/nn2.jpg"]]
        self.authors = [["Oleg"],
                        ["Nikita"],
                        ["Fedor", "Anton"]]
    def get_titles(self):
        return self.titles

    def get_articles_theme(self, num): # Возвращает массив словарей
        data = []
        num -= 1
        for i in range(len(self.articles_for_category[num])):
            data.append({"name" : self.articles_for_category[num][i],
                         "img" : self.images_for_category[num][i],
                         "author" : self.authors[num][i]})
        return data


mock_db = Data()
from .models import Autors, Articles, Subjects

def GetArticles(request):
    subjects = Subjects.objects.all()

    return render(request, 'bmstu_lab/topics.html', {'data' : subjects})

def GetArticle(request, id):
    articles_by_group = Articles.objects.filter(subject_id=id)

    return render(request, 'bmstu_lab/articles.html', {'data' :  articles_by_group})
