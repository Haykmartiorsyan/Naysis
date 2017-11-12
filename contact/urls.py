from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.contactView.as_view(), name='contact'),
]