from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy

from .forms import PageForm
from .models import Pages
from django.views.generic import ListView,DetailView,FormView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib import messages
# Create your views here.
# exclude

class PageList(ListView):
    model = Pages
    paginate_by = 10
    template_name = 'Pages/listPage.html'
    context_object_name = 'data'
    ordering = ['id']
def DeletePage(request,pk):
    if (int(pk)==Pages.objects.first().id):
        messages.error(request,"خطا در حذف آیتم انتخابی، لطفا مجددا تلاش نمایید.")
        return redirect(reverse('page_list'))
    try:
        x = Pages.objects.get(id=pk)
        messages.success(request,"آیتم با موفقیت حذف شد")
        x.delete()
    except ObjectDoesNotExist:
        messages.error(request, "چنین صفحه ای یافت نشد آيا مطمین هستید؟")


    return redirect(reverse('page_list'))


class PageAdd(FormView):
    template_name = 'Pages/addPage.html'
    form_class = PageForm
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        messages.success(self.request,"صفحه با موفقیت ایجاد شد!")
        form.save()
        return super(PageAdd, self).form_valid(form)
class EditPage(UpdateView):
    template_name = 'Pages/editPage.html'
    success_url = reverse_lazy('page_list')
    form_class = PageForm
    model = Pages
    def form_valid(self, form):
        messages.success(self.request,"با موفقیت ویرایش شد")
        return super().form_valid(form)

