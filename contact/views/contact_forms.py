from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from contact.form import Registerform


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
