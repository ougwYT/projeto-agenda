from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):

    first_name = models.CharField(
        "Primeiro nome",
        max_length=50,
    )

    last_name = models.CharField(
        "Sobrenome",
        max_length=50,
        blank=True,
    )

    phone = models.CharField(
        "Telefone",
        max_length=50,
    )

    email = models.EmailField(
        "E-mail",
        max_length=254,
        blank=True,
    )

    description = models.TextField(
        "Descrição",
        blank=True,
    )

    show = models.BooleanField(
        "Exibir",
        default=True,
    )

    picture = models.ImageField(
        "Foto",
        blank=True,
        upload_to="pictures/%Y/%m/",
    )

    category = models.ForeignKey(
        Category,
        verbose_name="Categoria",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
