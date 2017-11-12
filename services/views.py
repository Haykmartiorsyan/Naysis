from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from project.models import ServiceItems
# Create your views here.


class Services(generic.TemplateView):
    template_name = "services/index.html"

    def get_context_data(self, **kwargs):
        context = {}
        service_items = ServiceItems.objects.filter(is_active=True)

        context['service_items'] = service_items


        return context