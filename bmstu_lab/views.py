from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

class Data:
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

    def get_articles_theme(self, num):
        data = []
        num -= 1
        for i in range(len(self.articles_for_category[num])):
            data.append({"name" : self.articles_for_category[num][i],
                         "img" : self.images_for_category[num][i],
                         "author" : self.authors[num][i]})
        return data


mock_db = Data()

def hello(request): # Smth that user want might to see
    return render(request, 'bmstu_lab/index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})

def GetOrders(request):
    return render(request, 'bmstu_lab/orders.html', {'data' : {
        'current_date': date.today(),
        'orders': mock_db.get_titles()
    }})

def GetOrder(request, id):
    ids_category = [1, 2, 3]
    articles_for_category = [["Physics mechanics", "Physics quantum"],
                             ["Linear algebra", "Math for students"],
                             ["CNN for detection", "Function activation"]]
    articles_by_theme = dict(zip(ids_category, articles_for_category))
    print(mock_db.get_articles_theme(id))
    return render(request, 'bmstu_lab/order.html', {'data' :  mock_db.get_articles_theme(id)})

def fedor(request): #
    return HttpResponse("Hello Fedor")