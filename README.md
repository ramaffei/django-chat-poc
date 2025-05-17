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
## Uso con Docker

1. Construir e iniciar los servicios:
   ```bash
   docker-compose up --build

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
