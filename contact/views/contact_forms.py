from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from  contact.models import Contact
from django.core.exceptions import ValidationError
from django import forms
from contact.form import ContactForm

def create(request: HttpRequest) ->HttpResponse:
    form = ContactForm()
    if request.method == 'POST':
        context = {
                'form': ContactForm(request.POST)
            }
        return render(request, "contact/create.html",context)
    
    if form.is_valid():
            print('FORMULÁRIO VÁLIDO')
    else:
            print('FORMULÁRIO INVÁLIDO')


    context = {
        'form': ContactForm()
    }
    return render(request, "contact/create.html",context)
