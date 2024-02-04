from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان پست")
    short_description = models.TextField(verbose_name="توضیحات کوتاه")
    content = RichTextField(blank=True, null=True)
    url = models.SlugField(verbose_name="آدرس صفحه" )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ابجاد پست ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت پست")
    keyword = models.CharField(blank=True, null=True, max_length=150)