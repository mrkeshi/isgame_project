from django.db import models


class Contact(models.Model):
    def __init__(self, *args, **kwargs):
        x = super(Contact, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " border-error"
                    self.fields[f_name].widget.attrs['class'] = classes
        return x
    name=models.CharField(max_length=100)
    email=models.EmailField()
    description=models.TextField()