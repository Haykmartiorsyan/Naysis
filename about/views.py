from django.shortcuts import render
from django.views import generic

class About(generic.TemplateView):
    template_name = "about/index.html"

    def get_context_data(self, **kwargs):
        context = {}


        return context
