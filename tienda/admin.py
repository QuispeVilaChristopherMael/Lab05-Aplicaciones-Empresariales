from django.contrib import admin
from django.db import models
from .models import Categoria, Producto, Cliente


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "pub_date")
    search_fields = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "stock")
    search_fields = ("nombre",)
    actions = ["incrementar_stock_20"]

    @admin.action(description="Incrementar stock en 20 unidades")
    def incrementar_stock_20(self, request, queryset):
        filas_actualizadas = queryset.update(stock=models.F("stock") + 20)
        self.message_user(
            request,
            f"Se incrementó el stock de {filas_actualizadas} producto(s) en 20 unidades.",
        )


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("dni", "nombres", "apellidos", "email", "telefono")
    search_fields = ("nombres", "apellidos", "dni")
