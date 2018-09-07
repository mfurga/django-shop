from django.urls import path

from .views import ads_list, ads_create, ads_detial


app_name = 'ads'
urlpatterns = [
    path('', ads_list, name='list'),
    path('create', ads_create, name='create'),
    path('ad/<slug:slug>', ads_detial, name='detail')
]
