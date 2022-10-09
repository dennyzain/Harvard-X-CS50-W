from django.urls import path
from ramadhan import views

urlpatterns=[
    path('',views.index,name='ramadhan')
]