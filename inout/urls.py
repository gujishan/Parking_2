from django.conf.urls import url

from inout import views

urlpatterns = [
    url(r'carin/', views.carin, name='carin'),
    url(r'carin_tu/',views.carin_tu,name='carin_tu'),

    url(r'carout/', views.carout, name='carout'),
    url(r'carout_tu/', views.carout_tu, name='carout_tu'),

    url(r'pay/', views.pay, name='pay'),
]
