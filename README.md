# 🛒 Laboratorio 05 — Administrador con Django

**Curso:** Desarrollo de Aplicaciones Web  
**Tema:** Administrador con Django  
**Autor:** Christopher Quispe Y Jesus Olazabal 
**Institución:** Tecsup  
**Semana:** 05

---

## 📋 Descripción del proyecto

Este repositorio contiene el desarrollo del **Laboratorio 05**, consistente en la implementación de un panel de administración con **Django** para una aplicación de tienda. El proyecto incluye:

- Gestión de modelos (`Categoria`, `Producto`, `Cliente`)
- Registro y personalización del administrador de Django (`admin.py`)
- Capa estética personalizada con **django-jazzmin**
- Acción personalizada en lote para incrementar el stock de productos
- Migraciones de base de datos con SQLite3
- Usuario administrador para acceso al panel

---

## 🗂️ Estructura del proyecto

```
lab05/
├── manage.py
├── lab05/                 # Configuración del proyecto
│   ├── settings.py        # INSTALLED_APPS, JAZZMIN_SETTINGS, base de datos
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tienda/                # Aplicación de la tienda
│   ├── models.py          # Modelos: Categoria, Producto, Cliente
│   ├── admin.py           # ModelAdmin personalizados y acción en lote
│   ├── migrations/        # Migraciones de base de datos
│   ├── apps.py
│   ├── views.py
│   └── tests.py
├── db.sqlite3             # Base de datos local (NO subir a GitHub)
├── .gitignore             # Archivos excluidos de control de versiones
└── README.md              # Este archivo
```

---

## 🛠️ Modelos implementados

### 1. `Categoria`
Relación uno a muchos con `Producto`.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `nombre` | `CharField` (100) | Nombre de la categoría |
| `pub_date` | `DateTimeField` | Fecha de publicación (auto_now_add) |

### 2. `Producto`
Relación `ForeignKey` a `Categoria` (uno a muchos).

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `categoria` | `ForeignKey` | Categoría a la que pertenece |
| `nombre` | `CharField` (100) | Nombre del producto |
| `precio` | `DecimalField` | Precio del producto |
| `stock` | `IntegerField` | Cantidad en inventario |

### 3. `Cliente` (Tarea adicional)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `nombres` | `CharField` (100) | Nombres del cliente |
| `apellidos` | `CharField` (100) | Apellidos del cliente |
| `dni` | `CharField` (8, unique) | DNI único |
| `telefono` | `CharField` (15, blank) | Teléfono (opcional) |
| `direccion` | `CharField` (200, blank) | Dirección (opcional) |
| `email` | `EmailField` | Correo electrónico |
| `fecha_nacimiento` | `DateField` | Fecha de nacimiento |
| `fecha_publicacion` | `DateTimeField` | Fecha de creación (auto_now_add) |

Todos los modelos incluyen el método `__str__` para una mejor visualización en el admin.

---

## 🎨 Personalización del Administrador

### django-jazzmin
Se instaló y configuró el paquete **django-jazzmin** como primera entrada en `INSTALLED_APPS` (antes de `django.contrib.admin`) para mejorar el diseño visual del panel de administración.

### ModelAdmin personalizados

| Modelo | `list_display` | `search_fields` |
|--------|---------------|-----------------|
| `Categoria` | `id`, `nombre`, `pub_date` | `nombre` |
| `Producto` | `nombre`, `categoria`, `precio`, `stock` | `nombre` |
| `Cliente` | `dni`, `nombres`, `apellidos`, `email`, `telefono` | `nombres`, `apellidos`, `dni` |

### Acción personalizada en lote
Desde el módulo **Productos** del administrador, se puede seleccionar uno o más productos y ejecutar la acción:

> **"Incrementar stock en 20 unidades"**

Esta acción aumenta el campo `stock` de los productos seleccionados en 20 unidades usando `models.F("stock") + 20` y muestra un mensaje de confirmación.

---

## 🚀 Instalación y ejecución

### Requisitos previos
- Windows 10 o Windows 11
- Python 3.x instalado
- Pip (gestor de paquetes de Python)

### Pasos para correr el proyecto localmente

```bash
# 1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd lab05

# 2. Crear y activar entorno virtual
python -m venv myvenv
myvenv\Scripts\activate

# 3. Instalar dependencias
pip install django django-jazzmin

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario
python manage.py createsuperuser
#   Usuario: admin
#   Contraseña: Tecsup2019

# 6. Iniciar el servidor
python manage.py runserver
```

### Acceso al panel de administración

Una vez iniciado el servidor, visita:

```
http://127.0.0.1:8000/admin/
```

Ingresa con las credenciales del superusuario creadas anteriormente.

---

## ✅ Criterios de evaluación cubiertos

| Criterio | Estado |
|----------|--------|
| Registro correcto de modelos en el administrador | ✅ Implementado |
| Personalización de vista (`list_display`, `search_fields`) | ✅ Implementado |
| Acceso al panel con usuario administrador | ✅ Implementado |
| Operaciones CRUD desde el panel administrativo | ✅ Disponible |
| Tarea adicional: modelo `Cliente` | ✅ Implementado |
| Tarea adicional: personalización avanzada (jazzmin) | ✅ Implementado |
| Tarea adicional: acciones personalizadas en lote | ✅ Implementado |

---

## 🔒 Seguridad

- El archivo `.gitignore` excluye el entorno virtual, la base de datos SQLite (`db.sqlite3`), archivos de entorno (`.env`), credenciales y cualquier dato sensible.
- **Nunca subas** el archivo `db.sqlite3` ni el entorno virtual (`myvenv/`) a un repositorio público.
- La clave `SECRET_KEY` de Django está configurada solo para desarrollo local.

---

## 👨‍🏫 Para el profesor

Este proyecto cumple con todos los requisitos del Laboratorio 05 según la guía oficial del curso, incluyendo la corrección de erratas (`INSTALLED_APPS` con doble "L"), uso correcto de la app `tienda`, definición exacta del modelo `Cliente`, y la acción personalizada de incremento de stock en lote.


