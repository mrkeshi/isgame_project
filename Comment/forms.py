from django import forms
from .models import Comment

class ReplayCommentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ReplayCommentForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " border-bt-error"
                    self.fields[f_name].widget.attrs['class'] = classes

    message = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'message',
        'placeholder': 'پاسخ نظر',
        'class': 'form-control',
        'rows': 4,
    }), required=False, )