from django.contrib import admin

# Register your models here.
from Post.models import Articles


@admin.register(Articles)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','url','title']