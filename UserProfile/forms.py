from django import forms
from django.db.models import Q
from User import models
from django.core import validators
from django.forms import ModelForm, CharField, TextInput,Textarea,FileInput
from SiteModule import models

class RegisterForm(forms.Form):


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')

                    classes += " error-br"
                    self.fields[f_name].widget.attrs['class'] = classes


    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': ' border-[2px] w-full p-[14px]  outline-gray-500 border-red-500 transition-all font-IRsansLight ease-in border-gray-500 text-black-500 text-mxl  bg-white border-none max-sm:text-base outline-none focus:outline-gold-500 outline-1 font-light  ',
        'placeholder': 'لطفا نام خود را وارد نمایید.',
    }), required=False,)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': ' border-[2px] w-full p-[14px]  outline-gray-500 border-red-500 transition-all font-IRsansLight ease-in border-gray-500 text-black-500 text-mxl  bg-white border-none max-sm:text-base outline-none focus:outline-gold-500 outline-1 font-light  ',
        'placeholder': 'لطفا آدرس ایمیل خود را وارد نمایید'
    }), validators=[validators.EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': ' border-[2px] w-full p-[14px]  outline-gray-500 border-red-500 transition-all font-IRsansLight ease-in border-gray-500 text-black-500 text-mxl  bg-white border-none max-sm:text-base outline-none focus:outline-gold-500 outline-1 font-light  ',
        'placeholder': 'پسورد خود را وارد کنید'
    }), validators=[
        validators.MinLengthValidator(8),
        validators.MaxLengthValidator(38)
    ])
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': ' border-[2px] w-full p-[14px]  outline-gray-500 border-red-500 transition-all font-IRsansLight ease-in border-gray-500 text-black-500 text-mxl  bg-white border-none max-sm:text-base outline-none focus:outline-gold-500 outline-1 font-light  ',
        'placeholder': 'لطفا تکرار پسورد خود را وارد نمایید.'
    }), validators=[
        validators.MaxLengthValidator(38)
    ])


    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("پسورد با تکرار پسورد مطابقت ندارد.")
        return password_confirm

    def clean_username(self):
        user = models.User.objects.filter(
            Q(username=self.cleaned_data.get('username')) | Q(email=self.cleaned_data.get('email'))).exists()
        if user:

            raise forms.ValidationError("این نام کاربری از قبل وجود دارد.")
        return self.cleaned_data.get('username')


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'border w-full p-[14px]  outline-gray-500 transition-all ease-in font-IRsansLight border-gray-500 text-black-500 text-mxl  bg-white border-none max-sm:text-base outline-none focus:outline-gold-500 outline-1 font-light ',
        'placeholder': 'لطفا ایمیل یا نام کاربری خود را وارد نمایید',
         'style':'font-weight: 100'
    }), validators=[validators.EmailValidator])
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'border w-full p-[14px]  outline-gray-500 transition-all ease-in font-IRsansLight border-gray-500 text-black-500 text-mxl  bg-white border-none max-sm:text-base outline-none focus:outline-gold-500 outline-1 font-light ',
        'placeholder': 'پسورد خود را وارد کنید',
        'style': 'font-weight: 100'
    }))
    def clean_username(self):
        user = models.User.objects.filter(
            Q(username=self.cleaned_data.get('username')) | Q(email=self.cleaned_data.get('username'))).first()
        if user is None:
            raise forms.ValidationError('چنین یوزری یافت نشد لطفا دوباره چک کنید.')
        else:
            return user


class ResetPassword(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ایمیل یا نام کاربری',
        'id': 'email'
    }))

    def clean_username(self):
        user = models.User.objects.filter(
            Q(username__iexact=self.cleaned_data.get('username')) | Q(
                email__iexact=self.cleaned_data.get('username'))).first()

        if user is None:

            raise forms.ValidationError('')
        else:
            return user


class ResetPasswordConfirm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'رمز عبور',
        'id': 'password'
    }), min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'تکرار رمز عبور',
        'id': 'confirm_password'
    }), min_length=8)
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if (password == confirm_password):
            return confirm_password
        raise forms.ValidationError('')


