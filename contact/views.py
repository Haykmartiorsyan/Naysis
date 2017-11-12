from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .forms import ContactForm
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail, BadHeaderError

# Create your views here.


class contactView(TemplateView):
    template_name = 'contact/index.html'

    def get_context_data(self, **kwargs):
        context = {}

        return context


class contactView(generic.View):
    form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'contact/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            fullMessage = "<html><body>" \
                          "<p>Email From: {fromEmail}</p>" \
                          "<p>Phone Number : {phone} </p>"\
                          "<hr>" \
                          "<p>Subject: {subject}</p>" \
                          "<p>{message}</p>" \
                          "<p>Name: {name}</p>" \
                          "</body></html>".format(fromEmail=email, subject=subject, phone=phone, message=message, name=name)

            form.save()
            try:
                send_mail("Email From Naysis", fullMessage, email, ["info@naysis.com"])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return HttpResponseRedirect(request, self.template_name)

        return render(request, self.template_name, {'form': form})

