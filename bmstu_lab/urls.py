from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello") ,# default view for this application
    path("fedor", views.fedor, name="fedor" )
]