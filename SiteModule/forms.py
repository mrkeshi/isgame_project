
from django import forms
from django.forms import models, TextInput, NumberInput

from SiteModule.models import SocialMediaLink, PublicSettings,MediaGallery,Widget


class AddSocialForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        x = super(AddSocialForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " form-error"
                    self.fields[f_name].widget.attrs['class'] = classes

        return x



    class Meta:

        model = SocialMediaLink
        exclude=['user']
        widgets = {
            'is_setting': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "می توانید به این فیلد مقداری ندهید",
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "t.me/paressep28",
            }),
            'aparat': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "aparat.com/alireza81",
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "instagram/paressep28",
            }),
            'linkedin': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "linkedin.com/mrkaf_s",
            }),
            'facebook': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "facebook/mrkeshi.ir",
            }),
            'github': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "github.com/mrkaf",
            }),
            'youtube': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "youtube.com/alireza",
            }),

            'website': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "mrkeshi.ir",
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "paressep28@gmail.com",
            }),

            'twitter': forms.TextInput(attrs={
                'class': 'form-control h-100 ',
                'placeholder': "twitter.com/mrkafold",
            }),
        }

class SettingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        x = super(SettingForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " set-error"
                    self.fields[f_name].widget.attrs['class'] = classes
        return x
    class Meta:
        model=PublicSettings
        fields=["title","description","url","email","logoIcon","logoSite","post_per_homePage","post_per_cat","is_Register","is_Comment"]

        widgets={
            'title':TextInput(attrs={
                'id':'title',
                'placeholder':'عنوان سایت',
                'class':'form-control'
            }),
            'post_per_homePage':NumberInput(attrs={
                'class': 'form-control mb-4',
                'id': 'post_per_homePage',
            }),
            'post_per_cat': NumberInput(attrs={
                'class': 'form-control mb-4',
                'id': 'post_per_cat',
            }),
            'url': TextInput(attrs={
                'id': 'url',
                'placeholder': 'آدرس سایت',
                'class': 'form-control'
            }),
            'email': TextInput(attrs={
                'id': 'url',
                'placeholder': 'ایمیل اطلاع رسانی',
                'class': 'form-control mb-4'
            }),
            'logoIcon':forms.FileInput(attrs={
                'id':'input-file-max-fs',
                'class':'dropify',
            }),
            'logoSite': forms.FileInput(attrs={
                'id': 'input-file-max-fs2',
                'class': 'dropify'
            }),
            'description': forms.Textarea(attrs={
                'id': 'description',
                'placeholder': 'توضیحات کوتاه در مورد سایت',
                'class': 'form-control',
                'rows':4,
            }),
            'is_Register': forms.CheckboxInput(attrs={
                'id': 'is_Register',
                'class': 'new-control-input',
            }),
            'is_Comment':forms.CheckboxInput(attrs={
                'id':'is_Comment',
                'class':'new-control-input'
            })
        }


class GalleryForm(forms.ModelForm):
    class Meta:
        model=MediaGallery
        fields=["image"]
        widgets={
            'image':forms.FileInput(attrs={
                'id':'input-file-max-fs',
                'class':'custom-file-container__custom-file__custom-file-input',
            }),
        }

# ads banner

class BannerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        x = super(BannerForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " form-error"
                    self.fields[f_name].widget.attrs['class'] = classes
        return x

    class Meta:

        model = Widget
        fields = "__all__"

        widgets = {
            'urladbaner': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': " mr-keshi.ir/urladbanner"
            }),
            'imageurladbaner': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': " mr-keshi.ir/imag"
            }),
            'statusadbaner': forms.CheckboxInput(attrs={
                'class': 'custom-control-input',
                'id': 'gridCheck',
                'type': 'checkbox'
            })
        }

