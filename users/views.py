from django.shortcuts import render
from django.http import HttpResponse


def users_signin(request):
    return render(request, 'users/users_signin.html', {})
