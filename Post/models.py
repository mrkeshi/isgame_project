import datetime
from django.urls import reverse
from jalali_date import datetime2jalali
from jalali_date.fields import SplitJalaliDateTimeField


from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from User.models import User

from django.utils.text import slugify

class ArticleTags(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان تگ" ,unique=True)
    url = models.TextField(verbose_name="آدرس تگ", unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = slugify(self.title, allow_unicode=True)
        super(ArticleTags, self).save(*args, **kwargs)

class ArticleCategories(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان دسته" ,unique=True)
    url = models.TextField(unique=True, verbose_name="آدرس دسته بندی")

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.url = slugify(self.title, allow_unicode=True)
        super(ArticleCategories, self).save(args, kwargs)
    def get_absolute_url(self):
        return reverse('category_page',args=[self.title])
class Articles(models.Model):
    title = models.CharField(max_length=50, verbose_name= "عنوان پست" ,unique=True)
    short_description = models.TextField(verbose_name="توضیحات کوتاه")
    content = RichTextField( blank=True, null=True)
    url = models.SlugField(verbose_name="آدرس پست",unique=True)
    is_active = models.BooleanField(choices=((False,'پیش نویس'),(True,"نمایش عمومی")),default=False)
    is_pin = models.BooleanField(verbose_name="یین شده")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت پست")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    tags = models.ManyToManyField(ArticleTags, verbose_name="تگ ها", blank=True,null=True)
    categories = models.ManyToManyField(ArticleCategories, verbose_name="دسته ها", blank=True)
    image = models.ImageField(upload_to='Articles', null=True, blank=True)
    keyword =models.CharField(blank=True,null=True,max_length=150)
    previewtext=models.TextField(max_length=500)
    def __str__(self):
        return self.title + " | "

    def get_absolute_url(self):
        return reverse("single_post", args=[self.title])

    def save(self,*args, **kwargs):
        # self.created_date=
        self.url=slugify(self.title,allow_unicode=True)
        super(Articles, self).save(args,kwargs)


class DownloadBox(models.Model):
    title1=models.CharField(max_length=50,blank=True,null=True)
    title2=models.CharField(max_length=50,blank=True,null=True)
    title3=models.CharField(max_length=50,blank=True,null=True)
    title4=models.CharField(max_length=50,blank=True,null=True)
    link1=models.URLField(blank=True,null=True)
    link2=models.URLField(blank=True,null=True)
    link3=models.URLField(blank=True,null=True)
    link4=models.URLField(blank=True,null=True)
    Post=models.ForeignKey(Articles,on_delete=models.CASCADE)
    password=models.CharField(max_length=50,blank=True,null=True,default="پسورد ندارد.")