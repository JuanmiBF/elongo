from django.urls import path

from . import views

app_name = 'elongoApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('city/new', views.new_city, name='new_city'),
    path('city/list', views.list_city, name='list_city'),
    path('comparison', views.comparison, name='comparison'),
    path('city/list', views.list_city, name='list_city'),
    path('city/details/<int:city_id>', views.city_details, name='city_details'),
    path('electricData/new', views.new_electric_data, name='new_electric_data'),
    path('electricData/list', views.list_electric_data, name='list_electric_data'),
    path('city/details/<int:city_id>/<int:year>', views.city_details_year, name='city_details_year'),

]
