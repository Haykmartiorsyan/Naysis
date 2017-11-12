from django.conf.urls import url
from . import views

app_name='project'
urlpatterns = [
    url(r'^newproject/$', views.NewProject.as_view(), name='newproject'),
    url(r'^newproject/addproject$', views.NewProject.add_project, name='addproject'),
]


