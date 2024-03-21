from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.views.generic import ListView
from .models import Product,LinkDownload
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


def DeleteProduct(request, pk):
    item = Product.objects.filter(id=pk).first()
    if (item is not None):
        item.delete()
        messages.success(request,"محصول انتخابی با موفقیت حذف شد.")
    else:
       messages.error(request,"خطا در حذف آیتم محصول، لطفا مجددا تلاش نمایید.")
    return redirect(reverse('product_manage'))

class ProductManage(ListView):
    model = Product
    paginate_by = 10
    template_name = 'Shop/listProduct.html'
    context_object_name = 'data'
    ordering = ['id']




def EditProduct(request,pk):
    product=Product.objects.filter(id=pk).first()
    if(product==None):
        messages.error(request,"لینک اشتباه بود ای نادان!")
        return HttpResponseRedirect(reverse('product_manage'))
    form1=addProductForm(request.POST or None,request.FILES or None,instance=product)
    link=LinkDownload.objects.filter(Product=product).first()
    form2=LinkDownloadForm(request.POST or None,request.FILES or None,instance=link)
    if request.POST:
        if(form1.is_valid() and form2.is_valid()):
            thought = form1.save(commit=False)
            thought.author =request.user
            thought.save()
            box=form2.save(commit=False)
            box.Product=thought
            box.save()
            messages.success(request, "محصول با موفقیت ویرایش شد")
            return HttpResponseRedirect(reverse('product_manage'))
    return render(request,'Shop/editProduct.html',{
        'form':form1,
        'box_download':form2,
        'image':product.image,
        'link':link,
        'id':product.id
    })