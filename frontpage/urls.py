from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blaimage/', views.blaimage, name='blaimage')
]