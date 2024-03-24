from django import forms
from .models import Comment
class addCommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        exclude = ['updated','created', 'ip', 'active','post']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': "لطفا نام خود را وارد نمایید.",
                'class': "border w-full max-md:p-3 p-4 pr-11 outline-1 text-mxl outline-gray-500 transition-all ease-in border-gray-500 text-black-500 rounded ml-3 bg-white border-none outline-none focus:outline-black-500 font-IRsansLight",
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': "لطفا توضیحات کوتاه را وارد کنید"

            }),
            'email': forms.EmailField(attrs={
                'class': 'border w-full  p-4 max-md:p-3 pr-11 outline-1 text-mxl outline-gray-500 transition-all ease-in border-gray-500 text-black-500 rounded bg-white border-none outline-none focus:outline-black-500 font-IRsansLight',
                'placeholder': "لطفا ایمیل خود را وارد کنید"
            }),
        }