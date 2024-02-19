from django.http import HttpResponseRedirect
from django.shortcuts import render,reverse
from django.contrib import messages
from django.views.generic import ListView
from .models import Product
from .forms import LinkDownloadForm,addProductForm
# Create your views here.
def addProductView(request):
    form1=addProductForm(request.POST or None,request.FILES or None)
    form2=LinkDownloadForm(request.POST or None,request.FILES or None)
    if request.POST:
        if(form1.is_valid() and form2.is_valid()):
            thought = form1.save(commit=False)
            thought.author =request.user
            thought.save()
            box=form2.save(commit=False)
            box.Product=thought
            box.save()
            messages.success(request, "محصول با موفقیت ساخته شد")
            return HttpResponseRedirect(reverse('product_manage'))
    return render(request,'Shop/addProduct.html',{
        'form':form1,
        'box_download':form2
    })
class ProductManage(ListView):
    model = Product
    paginate_by = 10
    template_name = 'Shop/listProduct.html'
    context_object_name = 'data'
    ordering = ['id']