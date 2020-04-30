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
]
