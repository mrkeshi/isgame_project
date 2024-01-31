from django import forms
from django.db.models import Q
from .models import User
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
                    classes += " border-bt-error"
                    self.fields[f_name].widget.attrs['class'] = classes

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'نام',
    }), required=False, )
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'نام خانوادگی'
    }), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'ایمیل'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'نام کاربری'
    }), validators=[validators.EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'پسورد'
    }), validators=[
        validators.MinLengthValidator(8),
        validators.MaxLengthValidator(38)
    ])
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'تکرار پسورد'
    }), validators=[
        validators.MaxLengthValidator(38)
    ])
    checkBox = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'new-control-input'
    }), error_messages={
        'required': 'لطفا فیلد تایید قوانین را وارد کنید.'
    })

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("پسورد با تکرار پسورد مطابقت ندارد.")
        return password_confirm

    def clean_username(self):
        user = User.objects.filter(
            Q(username=self.cleaned_data.get('username')) | Q(email=self.cleaned_data.get('email'))).exists()
        if user:
            raise forms.ValidationError("این نام کاربری از قبل وجود دارد.")
        return self.cleaned_data.get('username')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'نام کاربری یا آدرس ایمیل'
    }), validators=[validators.EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'پسورد'
    }))
    checkBox = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'new-control-input'
    }),required=False)

    def clean_username(self):
        user = User.objects.filter(
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
        user = User.objects.filter(
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


class ProfileForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'firstname',
        'class': 'form-control',
        'placeholder': "لطفا نام خود را وارد کنید",

    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'lastname',
        'class': 'form-control',
        'placeholder': "لطفا نام خانوادگی خود را وارد کنید",

    }))

    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'id': 'firstname',
        'class': 'form-control',
        'placeholder': "لطفا نام خود را وارد کنید",

    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'firstname',
        'class': 'form-control',
        'placeholder': "لطفا نام خود را وارد کنید",

    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'firstname',
        'class': 'form-control',
        'placeholder': "لطفا نام خود را وارد کنید",

    }))


class SocialLinkForm(ModelForm):
    class Meta:
        model = models.SocialMediaLink
        fields = ["telegram","aparat","github","twitter","youtube","instagram","facebook","linkedin"]
        widgets = {
            'telegram': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username telegram'
            }),
            'aparat': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username aparat channel'
            }),
            'github': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '@github username'
            }),
            'twitter': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'twitter username'
            }),
            'youtube': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'youtube username'
            }),
            'instagram': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'instagram username'
            }),
            'facebook': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'facebook username'
            }),
            'linkedin': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'linkedin username'
            }),
        }


class UserProfileForm(ModelForm):
    class Meta:
        model=models.User
        fields=["first_name","last_name","about","avatar"]
        widgets={
            'first_name':TextInput(attrs={
                'id':'firs_tname',
                'placeholder':'نام',
                'class':'form-control'
            }),

            'last_name': TextInput(attrs={
                'id': 'last_name',
                'placeholder': 'نام خانوادگی',
                'class': 'form-control'
            }),
            'avatar':FileInput(attrs={
                'id':'file-upload',
                'class':'dropify'
            }),
            'about': Textarea(attrs={
                'id': 'aboutBio',
                'placeholder': 'درباره خود توضیح دهید',
                'class': 'form-control',
                'rows':10,
            }),

        }