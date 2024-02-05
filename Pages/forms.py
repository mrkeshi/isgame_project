from django import forms

from Pages.models import Pages


class PageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        x = super(PageForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " form-error"
                    self.fields[f_name].widget.attrs['class'] = classes
        return x
    class Meta:
        model = Pages
        exclude = ['updated_at', 'created_date','url', 'author', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "لطفا عنوان را وارد کنید",
                'class': "form-control ",
                'style': "background: none;height: 55px",
                'id':'inputname'
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': "لطفا توضیحات کوتاه را وارد کنید"

            }),
            'keyword': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': "لطفا کلمات کلیدی را وارد کنید"

            }),
            'is_active': forms.Select(attrs={
                'id': 'exampleFormControlSelect1',
                'class': 'form-control p-1'
            }),
            'url': forms.TextInput(attrs={
                'class': 'form-control text-left',
                'id': 'inputurl',
                'placeholder': "لطفا آدرسی را وارد کنید.",
                'style': "background: none;height: 55px"
            }),
        }