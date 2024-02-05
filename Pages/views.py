from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Pages
from django.views.generic import ListView,DetailView,FormView
from django.views.generic.edit import DeleteView
from django.contrib import messages
# Create your views here.
# exclude

class PageList(ListView):
    model = Pages
    paginate_by = 10
    template_name = 'Pages/listPage.html'
    context_object_name = 'data'

def DeletePage(request,pk):
    if (pk==1):
        messages.error(request,"خطا در حذف آیتم انتخابی، لطفا مجددا تلاش نمایید.")
    try:
        x = Pages.objects.get(id=pk)
        messages.success(request,"آیتم با موفقیت حذف شد")
        x.delete()
    except ObjectDoesNotExist:
        messages.error(request, "چنین فایلی یافت نشد آيا مطمپن هستید؟")


    return redirect(request.META.get('HTTP_REFERER'))


class AboutPage(FormView):
    pass

class AddPage(FormView):
    pass