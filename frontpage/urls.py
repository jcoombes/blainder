from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blaine_image>', views.blaimage, name='blaimage'),
]