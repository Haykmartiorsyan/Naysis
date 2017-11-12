from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.post_home, name='index'),
    url(r'^(?P<pk>\d+)/$', views.post_detail.as_view(), name="single-post"),
]