from django.shortcuts import render
from .items.dashboard_view import dasboard_class


# Create your items here.


class admin_panel:
    pass

# class dashboard(admin_panel):
#     def dashboard_view(self, request):
#         return render(request, 'dashbaord/dashbaord.html')


def header_component(request):
    return render(request,'component/header_component.html',{

    })