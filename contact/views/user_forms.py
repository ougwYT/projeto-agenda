from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from contact.form import Registerform, RegisterUpdateForm


def register(request: HttpRequest) -> HttpResponse:
    form = Registerform()
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário registrado")
            return redirect("contact:index")

    return render(
        request,
        "contact/register.html",
        {
            "form": form,
        },
    )


@login_required(login_url="contact:login")
def user_update(request: HttpRequest) -> HttpResponse:
    form = RegisterUpdateForm(instance=request.user)

    if request.method != "POST":
        return render(
            request,
            "contact/user_update.html",
            {
                "form": form,
            },
        )
    form = RegisterUpdateForm(data=request.POST, instance=request.user)
    if not form.is_valid():
        return render(
            request,
            "contact/user_update.html",
            {
                "form": form,
            },
        )
    form.save()
    return redirect("contact:user_update")


def login_view(request: HttpRequest) -> HttpResponse:
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Logado com sucesso")
            return redirect("contact:index")
        messages.error(request, "usuário ou senha incorretos")

    return render(
        request,
        "contact/login.html",
        {
            "form": form,
        },
    )

@login_required(login_url='contact:login')
def logout_view(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return redirect("contact:login")
