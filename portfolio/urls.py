from django.conf.urls import url
from . import views

app_name='portfolio'
urlpatterns = [
    url(r'^$', views.listing, name='index'),
]