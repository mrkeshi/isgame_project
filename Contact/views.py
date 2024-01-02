from django.shortcuts import render
from django.views.generic import FormView


# Create your views here.
class ContactView(FormView):
    template_name = ''