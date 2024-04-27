from django.urls import path
from . import views

urlpatterns = [
    path('', views.re, name='re'),
    path('recepie', views.recepie, name='recepie'),
    path('view', views.view, name='view'),
    path('search', views.search , name='search')
]