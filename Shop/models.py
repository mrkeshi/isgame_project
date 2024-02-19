from ckeditor.fields import RichTextField
from django.db import models

from User.models import User
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):

    title = models.CharField(max_length=50, verbose_name="عنوان پست", unique=True)
    short_description = models.TextField(verbose_name="توضیحات کوتاه")
    content = RichTextField(blank=True, null=True)
    url = models.SlugField(verbose_name="آدرس محصول")
    is_active = models.BooleanField(choices=((False, 'پیش نویس'), (True, "نمایش عمومی")), default=False)
    is_pin = models.BooleanField(verbose_name="یین شده")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت پست")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    image = models.ImageField(upload_to='Products', null=True, blank=True)
    keyword = models.CharField(blank=True, null=True, max_length=150)
    price=models.IntegerField(default=0,verbose_name="قیمت محصول")
    fprice=models.IntegerField(default=0,verbose_name="قیمت اولیه محصول")
    def __str__(self):
        return self.title + " | "
    def save(self, *args, **kwargs):
        self.url = slugify(self.title, allow_unicode=True)
        super(Product, self).save(args, kwargs)

class Transaction(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.IntegerField(default=0,verbose_name="هزینه")
    is_success=models.BooleanField()
class Wallet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    money=models.IntegerField(default=0)
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Orders(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.IntegerField(default=0,verbose_name="هزینه")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class LinkDownload(models.Model):
    file=models.FileField(upload_to='product/file')
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True)