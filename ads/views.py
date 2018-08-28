from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .scripts import RequestGETParse
from .forms import AdSearchFrom
from .models import Ad


def ads_list(request):
    ads = Ad.objects.all()

    if request.method == 'GET' and request.GET:
        form = AdSearchFrom(request.GET)

        res = {k: v for k, v in request.GET.items() if v}
        parser = RequestGETParse(ads)
        for k, v in res.items():
            try:
                getattr(parser, k)(v)
            except AttributeError:
                pass
        ads = parser.get_objects()
    else:
        form = AdSearchFrom()

    paginator = Paginator(ads, 1)
    page = request.GET.get('page')

    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {
        'ads': ads,
        'form': form
    }
    return render(request, 'ads/ads_list.html', context)
