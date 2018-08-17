from django.shortcuts import render


def ads_list(request):
    return render(request, 'ads/ads_list.html', {})
