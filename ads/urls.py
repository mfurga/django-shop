from django.urls import path

from .views import ads_list, ads_create


app_name = 'ads'
urlpatterns = [
    path('', ads_list, name='list'),
    path('create', ads_create, name='create')
]
