from django.shortcuts import render
from django.views.generic import TemplateView

class ContactView(TemplateView):

    template_name = 'function/contact.html'

contact = ContactView.as_view()
