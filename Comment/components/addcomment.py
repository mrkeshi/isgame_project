from django_unicorn.components import UnicornView


class AddcommentView(UnicornView):
    def submit(self):
        print(self.component_kwargs.get('email'))
