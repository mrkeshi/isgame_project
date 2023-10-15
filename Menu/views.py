from django.db.models import Count, F
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import FormView, UpdateView
from django.views import View
# Create your views here.
from django.views.generic.detail import BaseDetailView

from Menu.forms import AddMenuForm
from Menu.models import Menu


class MainMenu(TemplateView):
    template_name = 'Menu/Menus.html'

    def get_context_data(self, **kwargs):
        data = super(MainMenu, self).get_context_data(**kwargs)
        data['get_places'] = Menu.objects.all().values('place_menu').annotate(value_count=Count('place_menu')).values(
            'place_menu', 'value_count').order_by()
        print(data['get_places'])
        return data


class addMenu(FormView):
    template_name = 'Menu/addMenu.html'
    success_url = reverse_lazy('MangeMenu')
    form_class = AddMenuForm

    def get_context_data(self, **kwargs):
        if (self.kwargs['menu'] not in Menu.placeMenu):
            # Todo: send error message
            pass
        data = super(addMenu, self).get_context_data(**kwargs)
        data['places'] = Menu.placeMenu
        data['place'] = self.kwargs['menu']
        return data

    def form_valid(self, form):
        print("form valid")
        menu = self.kwargs.get('menu')
        if (menu in Menu.placeMenu):
            form.save()
        else:
            pass
            # Todo: send error message
        # Todo:send success message
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is not valid")
        return super(addMenu, self).form_invalid(form)


class MenuItem(View):
    def get(self, request, *args, **kwargs):
        place_menu = kwargs.get('menu')
        data = Menu.objects.filter(place_menu=place_menu).all()
        return render(request, "Menu/MenuItems.html", {
            'place': place_menu,
            'data': data
        })


class EditMenuItem(UpdateView):
    template_name = 'Menu/editMenu.html'
    success_url = reverse_lazy('MangeMenu')
    form_class = AddMenuForm

    def get_object(self, *args, **kwargs):
        menu = get_object_or_404(Menu, pk=self.kwargs['id'])
        return menu

    def get_context_data(self, **kwargs):
        if (self.kwargs['menu'] not in Menu.placeMenu):
            # Todo: send error message
            pass
        data = super(EditMenuItem, self).get_context_data(**kwargs)
        data['id'] = self.kwargs['id']
        data['place'] = self.kwargs['menu']
        return data


def edaitStatus(request):
    if request.method == 'POST':

        myid = request.POST.get('id')
        item=Menu.objects.filter(id=myid).first()
        if item is not None :

            if item.is_active:
                item.is_active=0
            else:
                item.is_active=1
            item.save()
            return  JsonResponse({
            'status': 'valid_count',
            'item':item.is_active})
        else:
            return JsonResponse({
            'status': 'invalid_count'})

    else:
        JsonResponse({
            'status': 'invalid_count' })



def deleteItem(request):
    if request.method == 'POST':

        myid = request.POST.get('id')
        item=Menu.objects.filter(id=myid).first()
        if item is not None :
            item.delete()
            return  JsonResponse({
            'status': 'valid_count',})
        else:
            return JsonResponse({
            'status': 'invalid_count'})

    else:
        JsonResponse({
            'status': 'invalid_count' })
