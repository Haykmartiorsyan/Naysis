from django.shortcuts import render
from django.views import generic
from .forms import ProjectForm
from django.shortcuts import render, redirect, HttpResponse
from . import main
import os
# Create your views here.
class NewProject(generic.TemplateView):
    template_name = "project/newproject.html"

    def get_context_data(self, **kwargs):
        context = {}


        return context
    @staticmethod
    def add_project(request):
        if request.method == "POST":

            projectForm = ProjectForm(request.POST)

            if projectForm.is_valid():
                if request.POST.get('password') == request.POST.get('repassword'):


                    projectForm.save()
                    #cmd = "/srv/envs/naysis/bin/python /srv/envs/naysis/src/Naysis/project/main.py '{name}' '{password}'".format(name=request.POST.get('projectname'), password=request.POST.get('password'))
                    #os.system(cmd)

                    main.main(request.POST.get('projectname'),request.POST.get('password'))
                    return HttpResponse("valid")

                else:
                    return HttpResponse("password aren't match")

            else:
                print(projectForm)
                return HttpResponse("error")
