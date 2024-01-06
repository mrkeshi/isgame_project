from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import FormView

from Contact.forms import ContactForm


# Create your views here.
class ContactView(FormView):
    template_name = 'Contact/contact.html'
    form_class = ContactForm
    success_url =reverse_lazy('contact')
    def form_valid(self, form):
        super().form_valid(form)
        messages.success(self.request, "درخواست شما با موفقیت ارسال شد. با تشکر از شما!")

