
from django import forms
from django.forms import models

from SiteModule.models import SocialMediaLink


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

    
