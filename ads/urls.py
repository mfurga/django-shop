from django.urls import path

from .views import ads_list


app_name = 'ads'
urlpatterns = [
    path('', ads_list, name='list')
]
