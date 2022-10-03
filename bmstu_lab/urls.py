from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetArticles),
    path('order/<int:id>/', views.GetArticle, name='order_url'), # ссылка url, которая показывает статьи
]