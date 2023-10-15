from .models import ArticleTags, ArticleCategories, Articles
from django import forms
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
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputname',
                'placeholder': "نام تگ",

            }, ),
            'url': forms.TextInput(attrs={
                'class': 'form-control text-left',
                'id': 'inputurl',
                'placeholder': " mr-keshi.ir /ca"
            }),

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
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputname',
                'placeholder': "نام دسته",

            }, ),
            'url': forms.TextInput(attrs={
                'class': 'form-control text-left',
                'id': 'inputurl',
                'placeholder': " mr-keshi.ir /ca"
            }),

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
        'placeholder': "لطف تگ ها را وارد کنید"
    }),required=False)
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
            # 'tags':forms.Textarea(attrs={
            #         'class': 'form-control',
            #         'rows': 3,
            #         'placeholder': "لطف تگ ها را وارد کنید"
            #
            # })

        }
