from django.urls import path

from . import views

app_name = 'elongoApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('city/new', views.new_city, name='new_city'),
    path('city/list', views.list_city, name='list_city'),
    path('comparison', views.comparison, name='comparison')
]
