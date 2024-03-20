from .models import ArticleTags, ArticleCategories, Articles,DownloadBox
from django import forms
import datetime
from jalali_date import datetime2jalali,date2jalali
from jalali_date.fields import GregorianToJalali, SplitJalaliDateTimeField
from jdatetime import datetime as jalali_datetime

from django.forms import models
from ckeditor.widgets import CKEditorWidget
class AddTagForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        x = super(AddTagForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " form-error"
                    self.fields[f_name].widget.attrs['class'] = classes
        return x
    class Meta:
        model = ArticleTags
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputname',
                'placeholder': "نام تگ",
            }, ),
        }
class AddCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        x = super(AddCategoryForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " form-error"
                    self.fields[f_name].widget.attrs['class'] = classes

        return x

    class Meta:

        model = ArticleCategories
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputname',
                'placeholder': "نام دسته",

            }, ),


        }

class AddArticleForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        x = super(AddArticleForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " form-error"
                    self.fields[f_name].widget.attrs['class'] = classes
        return x


    mytag=forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
        'placeholder': "لطفا تگ ها را وارد کنید"
    }),required=False)
    created_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control pointer','autocomplete':"off", 'data-jdp': '','placeholder': "انتخاب تاریخ..."}),required=False)



    class Meta:
        model = Articles
        exclude=['updated_at','created_date','url','author','tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "لطفا عنوان مطلب را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 55px"
            }),
            'short_description':forms.Textarea(attrs={
                'class':'form-control',
                'rows':6,
                'placeholder': "لطفا توضیحات کوتاه را وارد کنید"

            }),
            'previewtext':forms.Textarea(attrs={
                'class':'form-control',
                'rows':6,
                'placeholder': "لطفا متن پیش نمایش را بنویسید"
            }),
            'keyword': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': "لطفا کلمات کلیدی را وارد کنید"

            }),

            'image': forms.FileInput(attrs={
                'id':'exampleFormControlFile1',
                'class':'form-control-file'
            }),
            'is_pin':forms.CheckboxInput(attrs={
                'class':'new-control-input'
            }),
            'is_active':forms.Select(attrs={
                'id':'exampleFormControlSelect1',
                'class':'form-control p-1'
            }),
            'categories':forms.CheckboxSelectMultiple(attrs={
                'class': 'new-control-input'
            }),


        }

class DownloadBoxForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        x = super(DownloadBoxForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " form-error"
                    self.fields[f_name].widget.attrs['class'] = classes
        return x

    class Meta:
        model = DownloadBox
        fields="__all__"
        widgets = {
            'title1': forms.TextInput(attrs={
                'placeholder': "لطفا عنوان دانلود را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 42px"
            }),
            'title2': forms.TextInput(attrs={
                'placeholder': "لطفا عنوان دانلود را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 42px"
            }),
            'title3': forms.TextInput(attrs={
                'placeholder': "لطفا عنوان دانلود را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 42px"
            }),
            'title4': forms.TextInput(attrs={
                'placeholder': "لطفا عنوان دانلود را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 42px"
            }),
            'link1': forms.URLInput(attrs={
                'placeholder': "لطفا لینک دانلود را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 42px"
            }),

            'link2': forms.URLInput(attrs={
                'placeholder': "لطفا لینک دانلود را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 42px"
            }),
            'link3': forms.URLInput(attrs={
                'placeholder': "لطفا لینک دانلود را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 42px"
            }),
            'link4': forms.URLInput(attrs={
                'placeholder': "لطفا لینک دانلود را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 42px"
            }),
            'password': forms.TextInput(attrs={
                'placeholder': "لطفا پسورد فایل را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 42px"
            }),
        }
