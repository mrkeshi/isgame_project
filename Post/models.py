from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from User.models import User

from django.utils.text import slugify

class ArticleTags(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان تگ")
    url = models.TextField(verbose_name="آدرس تگ", unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = slugify(self.title, allow_unicode=True)
        super(ArticleTags, self).save(args, kwargs)

class ArticleCategories(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان دسته")
    url = models.TextField(unique=True, verbose_name="آدرس دسته بندی")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = slugify(self.title, allow_unicode=True)
        super(ArticleCategories, self).save(args, kwargs)

class Articles(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان پست")
    short_description = models.TextField(verbose_name="توضیحات کوتاه")
    content = RichTextField( blank=True, null=True)
    url = models.SlugField(verbose_name="آدرس پست")
    is_active = models.BooleanField(choices=((False,'پیش نویس'),(True,"نمایش عمومی")),default=False)
    is_pin = models.BooleanField(verbose_name="یین شده")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ابجاد پست ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت پست")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    tags = models.ManyToManyField(ArticleTags, verbose_name="تگ ها", blank=True,null=True)
    categories = models.ManyToManyField(ArticleCategories, verbose_name="دسته ها", blank=True)
    image = models.ImageField(upload_to='Articles', null=True, blank=True)
    keyword =models.CharField(blank=True,null=True,max_length=150)
    def __str__(self):
        return self.title + " | "
    
    def save(self,*args, **kwargs):

        self.url=slugify(self.title,allow_unicode=True)
        super(Articles, self).save(args,kwargs)