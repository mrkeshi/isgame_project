from django_unicorn.components import UnicornView
from django import forms
from django.contrib import messages
from ..models import Comment
from utils import Http_service
from SiteModule.models import Newsletter as news


class AddcommentForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=50, required=True)
    message = forms.CharField(required=True)


class AddcommentView(UnicornView):
    form_class = AddcommentForm
    email = ""
    name = ""
    message = ""
    postId = ''
    status = False

    def mount(self):
        if(len(self.component_args)>0):
            kwarg = self.component_args[0]
            self.postId = kwarg
        return super().mount()

    def submit(self):
        if self.is_valid():
            self.status = True
            comm = Comment(email=self.email, name=self.name, message=self.message,post_id=self.postId,
                           ip=Http_service.get_client_ip(self.request))
            comm.save()
            try:
                ne = news.objects.get(email=self.email)
            except Exception:
                ne = news(email=self.email, ip=Http_service.get_client_ip(self.request), name=self.name)
                ne.save()
            self.email = ""
            self.name = ""
            self.message = ""
        else:

            print("not validated")
        return True
