from django_unicorn.components import UnicornView
from django import forms
from django.contrib import messages
class AddcommentForm(forms.Form):
    name=forms.CharField(max_length=30,required=True)
    email=forms.EmailField(max_length=50,required=True)
    message=forms.CharField(required=True)
class AddcommentView(UnicornView):
    form_class=AddcommentForm
    email=""
    name=""
    message=""
    postId=''
    status=False

    def mount(self):
        kwarg = self.component_args[0]
        self.postId=kwarg
        return super().mount()

    def submit(self):
        if self.is_valid():
            self.status = True
            self.email=""
            self.name=""
            self.message=""


        else:

            print("not validated")
        return True