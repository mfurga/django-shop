from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.utils import timezone

from .scripts import RequestGETParse
from .forms import AdSearchFrom, AdForm
from .models import Ad, Image


def ads_list(request):
    ads = Ad.objects.all()

    if request.method == 'GET':
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

    paginator = Paginator(ads, 3)
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


@login_required(login_url='/account/signin')
def ads_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            category = form.cleaned_data.get('category')
            description = form.cleaned_data.get('description')
            condition = form.cleaned_data.get('condition')
            location = form.cleaned_data.get('location')
            price = form.cleaned_data.get('price')
            phone_number = form.cleaned_data.get('phone')
            time = timezone.now()

            photo = form.cleaned_data.get('photo')
            photo2 = form.cleaned_data.get('photo2')
            photo3 = form.cleaned_data.get('photo3')
            photo4 = form.cleaned_data.get('photo4')
            author = request.user

            has_photo = True if photo else False

            ad = Ad(title=title, category=category, description=description,
                    condition=condition, location=location, phone_number=phone_number,
                    price=price, pub_date=time, author=author, has_photo=has_photo)

            ad.save()

            Image.objects.create(ad=ad, image=photo, prime=True) if photo else None
            Image.objects.create(ad=ad, image=photo2, prime=False) if photo2 else None
            Image.objects.create(ad=ad, image=photo3, prime=False) if photo3 else None
            Image.objects.create(ad=ad, image=photo4, prime=False) if photo4 else None

            messages.success(request, _('The ad has been created.'))
            return redirect('ads:list')
    else:
        form = AdForm()

    return render(request, 'ads/ads_create.html', {'form': form})


def ads_detial(request, slug):
    ad = get_object_or_404(Ad, slug=slug)
    return render(request, 'ads/ads_detail.html', {'ad': ad})
