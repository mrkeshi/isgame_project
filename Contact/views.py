from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.views.generic.list import ListView

from django.views.generic import FormView, DetailView

from Contact.forms import ContactForm
from .models import Contact

# Create your views here.
class ContactView(FormView):

    template_name = 'Contact/contact.html'
    form_class = ContactForm
    success_url =reverse_lazy('contact')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "درخواست شما با موفقیت ارسال شد. با تشکر از شما!")
        con = Contact(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            description=form.cleaned_data['description']
        )
        con.save()
        return response



# for admin
class ContactList(ListView):
    model = Contact
    paginate_by = 10
    template_name = 'Contact/contactList.html'
    context_object_name = "list"
    ordering = ['is_Displayed','-date']


def Delete_Contact(request, pk):
    item = Contact.objects.filter(id=pk).first()
    if (item is not None):
        item.delete()
        messages.success(request,"آیتم انتخابی با موفقیت حذف شد.")
    else:
       messages.error(request,"خطا در حذف آیتم انتخابی، لطفا مجددا تلاش نمایید.")
    return redirect(reverse('contact_list'))


class SingleContact(DetailView):
    model = Contact
    template_name = "Contact/SingleContact.html"
    context_object_name = 'c'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        contact = self.get_object()
        contact.is_Displayed = True
        contact.save()
        return context