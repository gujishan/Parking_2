from django.shortcuts import redirect
from django.urls import reverse


def my_login(func):
    def inner(request, *args, **kwargs):
        cookie = request.session.get('login_user_name')
        if cookie:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('root:login'))
    return inner
