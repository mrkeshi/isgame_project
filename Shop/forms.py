from django import forms
from .models import Product, LinkDownload


class addProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        x = super(addProductForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " form-error"
                    self.fields[f_name].widget.attrs['class'] = classes
        return x
    class Meta:
        model = Product
        exclude = ['updated_at','created_date', 'url', 'author']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "لطفا عنوان محصول را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 55px"
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': "لطفا توضیحات کوتاه را وارد کنید"

            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "لطفا قیمت محصول را به ریال وارد کنید"
            }),
            'fprice': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "لطفا قیمت محصول را به ریال وارد کنید"
            }),
            'keyword': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': "لطفا کلمات کلیدی را وارد کنید"

            }),
            'image': forms.FileInput(attrs={
                'id': 'exampleFormControlFile1',
                'class': 'form-control-file'
            }),
            'is_pin': forms.CheckboxInput(attrs={
                'class': 'new-control-input'
            }),
            'is_active': forms.Select(attrs={
                'id': 'exampleFormControlSelect1',
                'class': 'form-control p-1'
            }),

        }

class LinkDownloadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        x = super(LinkDownloadForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " form-error"
                    self.fields[f_name].widget.attrs['class'] = classes
        return x

    class Meta:
        model = LinkDownload
        exclude=['product']
        widgets = {
            'file': forms.FileInput(attrs={
                'placeholder': "لطفا فایلی را جهت آپلود انتخاب کنید",
                'class': "form-control ",
            }),
        }