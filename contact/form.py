
from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({
            'placeholder':'Escreva aqui',
            'class':'class-a class-b'
        })

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

        # widgets: ClassVar = {
        #     'first_name': forms.TextInput(
        #         attrs={'placeholder':'Escreva aqui','class':'class-a class-b'}),
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error(
            'first_name', ValidationError('Mensagem de erro', code='invalid')
        )
        return super().clean()
