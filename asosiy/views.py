from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import *

def register(request):
    if (request.method == 'POST'
            and
        request.POST.get("p") == request.POST.get("p2")):
        User.objects.create_user(
            username= request.POST.get("l"),
            password= request.POST.get("p"),
        )
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username = request.POST.get("l"),
            password = request.POST.get("p")
        )
        if user is not None:
            return redirect("/")
        login(request, user)
        return redirect("/maqolalar")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("/")

class MaqolaView(View):
    def post(self, request):
        forma = MaqolaForm(request.POST)
        if forma.is_valid():
            forma.save()
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                "maqolalar": Maqola.objects.filter(muallif__user=request.user),
                'form': MaqolaForm()
            }
            return render(request, 'maqolalar.html', data)
        return redirect('/')


class Bitta_mView(View):
    def get(self, request, pk ):
        data = {
            'maqola' : Maqola.objects.get(id=pk)
        }
        return render(request, 'maqola.html', data)




