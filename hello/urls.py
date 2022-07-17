
from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name='index'),
    path('date',views.date,name='date'),
    path('denny',views.denny,name='name'),
    path('<str:name>',views.greet,name='greet'),
]