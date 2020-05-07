from django.conf.urls import url

from root import views

urlpatterns = [
    url(r'root/', views.root, name='root'),
    url(r'login/', views.login, name='login'),
    url(r'registered/', views.registered, name='registered'),
    url(r'getro/', views.getro, name='get_ro'),
    url(r'rmro/(\d+)', views.rmro, name='rmro'),
    url(r'updatero/(\d+)', views.updatero, name='updatero'),
    url(r'findro/', views.findro, name='findro'),
    url(r'incar/', views.incar, name='incar'),
    url(r'allcar/', views.allcar, name='allcar'),
    url(r'findc/', views.findc, name='findc'),
    url(r'price/', views.price, name='price'),
    url(r'income/', views.income, name='income'),
    url(r'tu_car', views.tu_car, name='tu_car'),
    url(r'tu_money/', views.tu_money, name='tu_money'),
    url(r'findmoney', views.findmoney, name='findmoney'),
]
