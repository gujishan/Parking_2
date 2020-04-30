from django.conf.urls import url

from Car_w import views

urlpatterns = [
    url(r'addcw/', views.addcw, name='addcw'),
    url(r'showcw/', views.showcw, name='showcw'),
    url(r'rmcw/(\d+)', views.rmcw, name='rmcw'),
    url(r'updatecw/(\d+)', views.updatecw, name='updatecw'),
    url(r'findcs/', views.findcw, name='findcw'),
]
