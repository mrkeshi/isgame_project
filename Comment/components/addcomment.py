from django_unicorn.components import UnicornView
from django import forms

class AddcommentForm(forms.Form):
    name=forms.CharField(max_length=30,required=True)
    email=forms.EmailField(max_length=50,required=True)
    message=forms.CharField(required=True)
class AddcommentView(UnicornView):
    form_class=AddcommentForm
    email=""
    name=""
    message=""

    def submit(self):
        if self.is_valid():  # استفاده از متد is_valid برای بررسی اعتبار فرم
            print("is Valid")
            # print(self.form_class.cleaned_data['email'])  # دسترسی به ایمیل از داده‌های پاک‌سازی شده فرم
        else:
            print("not validated")