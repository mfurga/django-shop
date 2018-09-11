from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import SigninForm


def users_signin(request):
    next_page = request.GET.get('next') or reverse('ads:list')
    invalid_credentials = None
    form = SigninForm()

    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
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


def users_logout(request):
    logout(request)
    messages.success(request, _('Logout successfully.'))
    return redirect('ads:list')
