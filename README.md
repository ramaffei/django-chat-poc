# Chat App - Prueba Técnica

Este proyecto es una aplicación de chat en tiempo real utilizando Django, Django REST Framework y Channels. La base de datos utilizada es PostgreSQL y la comunicación en tiempo real se gestiona con WebSockets a través de Django Channels y Redis.

## Progreso

- [x] Crear proyecto Django (commit inicial)
- [x] Instalar paquetes necesarios
- [x] Configurar PostgreSQL
- [x] Configurar Docker y Docker Compose
- [ ] Implementar CRUD para salas de chat
- [ ] Configurar websockets con Channels
- [ ] Crear interfaz simple para acceder a salas y chatear

## Requisitos

- Python 3.10+
- Virtualenv (`venv`)
- Docker + Docker Compose

## Instalación y configuración inicial

1. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Crear archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```env
   POSTGRES_DB=chat_db
   POSTGRES_USER=chat_user
   POSTGRES_PASSWORD=chat_password
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   ```
4. Uso con Docker
  Construir e iniciar los servicios:
   ```bash
   docker-compose up --build

### CRUD de Salas de Chat

- Se creó la aplicación Django `rooms` para manejar la lógica de las salas de chat.
- Se agregó la app `rooms` al archivo de configuración `INSTALLED_APPS` en `settings.py`.
- Se creó el modelo `Room` con los campos: `name`, `description`, `created_at`.
- Se aplicaron migraciones para crear la tabla en la base de datos PostgreSQL.
- Se registró el modelo en el panel de administración para permitir gestión manual de salas.
- Se creó el archivo `rooms/serializers.py`.
- Se definió la clase `RoomSerializer` utilizando `ModelSerializer`.
- Se expusieron los campos: `id`, `name`, `description`, `created_at`, siendo `id` y `created_at` de solo lectura.
- Se implementó un `RoomViewSet` con `ModelViewSet` de DRF.
- Se aplicó un permiso personalizado `IsAdminOrReadOnly`.
- Se configuraron rutas REST con `DefaultRouter`.
- Los endpoints permiten listar a cualquier usuario.
- Solo usuarios autenticados con `is_staff=True` pueden crear, editar o eliminar salas.

## Estructura del proyecto

- `chat_project/`: Configuración principal de Django.
- `requirements.txt`: Dependencias del proyecto.
- `.env`: Variables de entorno (no se sube al repositorio).
- `manage.py`: Script para ejecutar comandos de Django.

## Sobre el uso de `decouple`

Para manejar la configuración sensible (como credenciales de la base de datos), se utiliza la librería [`python-decouple`](https://github.com/henriquebastos/python-decouple).

**Ventajas de usar `decouple`:**

- Mantiene las variables sensibles fuera del código fuente.
- No acopla la configuración al entorno de desarrollo.
- Es una solución simple, clara y Pythonic.
- A diferencia de soluciones más complejas como `django-environ`, `decouple` es liviano y rápido de configurar, ideal para pruebas técnicas y proyectos pequeños.

## Entorno y configuración

La aplicación se comporta distinto según la variable `ENVIRONMENT`. Los valores posibles son:

- `Local`: entorno de desarrollo local. Acceso total al admin (`/admin`), con archivos estáticos.
- `DEV`: entorno de desarrollo con Docker. Admin habilitado, archivos estáticos disponibles.
- `STG` y `PRD`: entornos de staging o producción. Se deshabilita por completo la vista `/admin`, y todas las rutas que no comienzan con `/api/` devolverán un JSON `404`.

### Endpoints: Salas de Chat

- `GET /api/rooms/`: Listar todas las salas (público)
- `POST /api/rooms/`: Crear una nueva sala (requiere autenticación y permisos de administrador)

## 🔐 Autenticación de administrador (Bearer Token)

Las operaciones de crear, editar y eliminar salas requieren autenticación.

Para obtener un token:
```bash
curl -X POST -d "username=admin&password=admin123" http://localhost:8000/api/token/