from django.shortcuts import render
from django.views import generic
from project.models import Slider
# Create your views here.


class Home(generic.TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = {}

        slider_image = Slider.objects.filter(is_active=True)

        context['slider_image'] = slider_image

        return context