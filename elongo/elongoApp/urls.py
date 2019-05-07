from django.urls import path

from . import views

app_name = 'elongoApp'
urlpatterns = [
    path('', views.index, name='index'),
]