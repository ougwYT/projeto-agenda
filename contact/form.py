from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    picture= forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*',
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite aqui",
            }
        ),
        label="Primeiro nome",
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite aqui",
            }
        ),
        label="sobrenome",
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite seu número aqui",
            }
        ),
        label="telefone",
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "coloque seu Email aqui",
            }
        ),
    )

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
            "picture",
        )

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name and first_name == last_name:
            msg = ValidationError(
                "Primeiro nome não pode ser igual ao sobrenome.",
                code="invalid",
            )

            self.add_error("first_name", msg)
            self.add_error("last_name", msg)

        return cleaned_data

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name and any(char.isdigit() for char in first_name):
            raise ValidationError(
                "Números não são aceitos neste campo.",
                code="invalid",
            )

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if last_name and any(char.isdigit() for char in last_name):
            raise ValidationError(
                "Números não são aceitos neste campo.",
                code="invalid",
            )

        return last_name

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if not phone:
            return phone

        if not phone.isdigit():
            raise ValidationError(
                "O telefone deve conter apenas números.",
                code="invalid",
            )

        if len(phone) not in (10, 11):
            raise ValidationError(
                "O telefone deve conter 10 ou 11 dígitos.",
                code="invalid",
            )

        return phone
