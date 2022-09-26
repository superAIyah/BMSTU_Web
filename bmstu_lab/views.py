from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

def hello(request): # Smth that user want might to see
    return render(request, 'bmstu_lab/index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})

def GetOrders(request):
    return render(request, 'bmstu_lab/orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Книга с картинками', 'id': 1},
            {'title': 'Бутылка с водой', 'id': 2},
            {'title': 'Коврик для мышки', 'id': 3},
        ]
    }})

def GetOrder(request, id):
    return render(request, 'bmstu_lab/order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})

def fedor(request): #
    return HttpResponse("Hello Fedor")