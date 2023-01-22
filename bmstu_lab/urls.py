from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.GetArticles),
    path('order/<int:id>/', views.GetArticle, name='order_url'), # ссылка url, которая показывает статьи
    path('api/register/', SignupView.as_view()),
    path('api/csrf_cookie/', GetCSRFToken.as_view()),
    path('api/authenticated/', CheckAuthenticatedView.as_view()),
    path('api/register/', SignupView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/logout/', LogoutView.as_view()),
    path('api/delete/', DeleteAccountView.as_view()),
    path('api/get_users/', GetUsersView.as_view()),
    path('api/user/', GetUserProfileView.as_view())
]