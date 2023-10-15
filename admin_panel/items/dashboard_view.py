from django.shortcuts import render


class dasboard_class:
    def dashboard_view(request):
        return render(request, 'dashbaord/dashbaord.html')
