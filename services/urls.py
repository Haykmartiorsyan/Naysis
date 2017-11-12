from django.conf.urls import url
from . import views

app_name='services'
urlpatterns = [
    url(r'^$', views.Services.as_view(), name='index'),
]