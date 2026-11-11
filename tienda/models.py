from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos",
    )
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


class Cliente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
