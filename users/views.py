from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

from .forms import SigninForm, SignupForm
import requests


def users_signin(request):
    next_page = request.GET.get('next') or reverse('ads:list')
    invalid_credentials = None
    form = SigninForm()

    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            invalid_credentials = True

            if user is not None:
                invalid_credentials = False
                login(request, user)
                messages.success(request, _('Logged in successfully.'))
                return HttpResponseRedirect(next_page)

    context = {
        'form': form,
        'invalid_credentials': invalid_credentials
    }
    return render(request, 'users/users_signin.html', context)


def users_signup(request):
    form = SignupForm()
    recaptcha_respone = False

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            recaptcha_respone = request.POST.get('g-recaptcha-response')

            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_respone
            }
            res = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data).json()
            if res['success']:
                User.objects.create_user(username=username, password=password)
                messages.success(request, _('The account has been created. You can log in now.'))
                return redirect('users:signin')

    context = {
        'form': form,
        'recaptcha_respone': recaptcha_respone
    }
    return render(request, 'users/users_signup.html', context)


def users_logout(request):
    logout(request)
    messages.success(request, _('Logout successfully.'))
    return redirect('ads:list')
