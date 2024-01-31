from django import forms
class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class')
                    classes += " border border-red-500 "
                    self.fields[f_name].widget.attrs['class'] = classes
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'appearance-none block w-full text-base bg-gray-200 text-black-500 bg-gray-300 focus:outline-none transition ease-in focus:border  rounded py-3 px-4 mb-3 leading-tight  h-14 max-sm:h-12 focus:bg-white ',
        'id':'name',
        'placeholder':'لطفا نام خود را وارد نمایید.',
    }))
    email=forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'class':'appearance-none block w-full text-base bg-gray-200 text-black-500 bg-gray-300  rounded py-3 px-4 mb-3 leading-tight  h-14 focus:outline-none max-sm:h-12 transition ease-in focus:border focus:bg-white',
        'id':'email',
        'placeholder':'لطفا ایمیل خود را وارد نمایید.'
    }))
    description=forms.CharField(widget=forms.Textarea(attrs={
        'class':'appearance-none block w-full text-base bg-gray-200 text-black-500 bg-gray-300 rounded py-3 px-4 mb-5 leading-tight focus:outline-none transition ease-in focus:border focus:bg-white',
        'id':'textarea',
        'placeholder':'این متن پیغام شما می باشد.',
        'cols':'15',
        'rows':'6'
    }))
