from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.forms import UserRegisterForm


# Create your views here.
def login_request(request):
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():
                data = form.cleaned_data

                usuario = data.get('username')
                contrasenia = data.get('password')

                user = authenticate(username=usuario, password=contrasenia)

                if user:
                    login(request, user)

            return redirect('/')

        form = AuthenticationForm()
        contexto = {
            "form": form
        }
        return render(request, "accounts/login.html", contexto)


def register_request(request):
    if request.method == "POST":
       # form = UserCreationForm(request.POST)#
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("Login")

    #form = UserCreationForm()#
    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request,"accounts/registro.html",contexto)


def logout_view(request):
    logout(request)
    return render(request, "templates/accounts/logout.html")
