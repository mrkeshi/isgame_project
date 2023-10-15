from .models import Menu
from django import forms
from django.forms import models


class AddMenuForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        x = super(AddMenuForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " form-error"
                    self.fields[f_name].widget.attrs['class'] = classes
        return x

    class Meta:

        model = Menu
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputname',
                'placeholder': "نام آیتم",


            },),
            'url': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputurl',
                'placeholder': " mr-keshi.ir /"
            }),
            'sort': forms.TextInput(attrs={
                'class': 'form-control ',
                'id': 'inputsort',
                'placeholder': " ترتیب نمایش: مثلا 1"
            }),
            'icon_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputfont',
                'placeholder': "fa fa-home"
            }),
            'icon_color': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputcolor',
                'type': 'color'
            }),

            'place_menu': forms.Select(attrs={
                'class': 'form-control p-1',
                'id': 'inputplace',
                'type': 'color',

            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'custom-control-input',
                'id': 'gridCheck',
                'type': 'checkbox'
            })
        }

    def clean_place_menu(self):
        x = self.cleaned_data.get('place_menu')
        if x not in Menu.placeMenu:
            pass
        # Todo send error mesage

        return x
