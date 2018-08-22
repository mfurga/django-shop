from django.shortcuts import render

from .models import Ad


def ads_list(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ads_list.html', {'ads':ads})
