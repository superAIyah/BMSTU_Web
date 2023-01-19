from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('api/register/', SignupView.as_view()),
    path('api/csrf_cookie/', GetCSRFToken.as_view())
]