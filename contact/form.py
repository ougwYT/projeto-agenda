from typing import ClassVar

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
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
        widgets: ClassVar = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Digite aqui",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Digite aqui",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Digite seu número aqui",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Coloque seu e-mail aqui",
                }
            ),
            "picture": forms.FileInput(
                attrs={
                    "accept": "image/*",
                }
            ),
        }

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

class Registerform(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )

    last_name = forms.CharField(
        required=True,
        min_length=3,
    )

    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error(
                "email", ValidationError("já existe este e-mail", code="invalid")
            )

        return email


class RegisterUpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Use the same password as before.",
        required=False,
    )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get("password1")

        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                self.add_error("password2", ValidationError("Senhas não batem"))

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    "email", ValidationError("já existe este e-mail", code="invalid")
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error("password1", ValidationError(errors))

        return password1

    class Meta:
        model = User

        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
        )
