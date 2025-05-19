# 💬 Chat App - Prueba Técnica

Aplicación de chat en tiempo real desarrollada con Django, Django REST Framework, Channels, WebSockets y PostgreSQL. Redis se utiliza como backend de Channel Layers.

---

## 🚀 Tecnologías

- Django 5.x
- Django REST Framework
- Django Channels
- WebSockets
- PostgreSQL
- Redis
- Docker + Docker Compose

---

## 📁 Estructura

- `chat_project/`: Configuración principal Django.
- `rooms/`: Módulo para gestionar salas de chat (modelo, API REST).
- `chat/`: Funcionalidad WebSocket (consumidores, lógica de chat).
- `templates/`: Frontend HTML renderizado por Django.
- `static/`: Archivos JS y CSS.
- `docker-compose.yml`: Configuración de contenedores.

---

## ⚙️ Variables de entorno (.env)

Ejemplo de `.env`:

```env
POSTGRES_DB=chat_db
POSTGRES_USER=chat_user
POSTGRES_PASSWORD=chat_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

ENVIRONMENT=Local  # Opciones: Local, DEV, STG, PRD
```

---

## 🐳 Uso con Docker

1. Crear `.env` en la raíz (ver arriba).
2. Construir e iniciar:

```bash
docker compose up --build
```
3. Con el contenedor iniciado migrar las base de datos:
```bash
docker compose exec web python manage.py migrate
```
> Luego accedé a la app en: [http://localhost:8000](http://localhost:8000)

---

## 💻 Uso con entorno virtual (`venv`)

1. Crear y activar entorno:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```
3. Migrar base de datos:

```bash
python manage.py migrate
```

4. Iniciar servidor de desarrollo:

```bash
python manage.py runserver
```

---
## 🔐 Seguridad Enpoint Salas

- Se debe crear el usuario admin utilizando el comando 
```bash
python manage.py createsuperuser
``` 
ingresando username, email y passowrd
- Se puede editar salas utilizando el panel de administracion [http://localhost:8000/admin](http://localhost:8000/admin)
- Para los endpoints se debe solicitar un Bearer Token a /api/token con un json body con username y password 
- 

## ✅ Endpoints TOKEN (Admin)

| Método | Endpoint             | Descripción                        |
|--------|----------------------|-------------------------------------------------------|
| POST    | `/api/token/`        | Solicitar Token de                        Acceso                            |
---

## ✅ Endpoints REST (Salas)

| Método | Endpoint             | Descripción                        |
|--------|----------------------|------------------------------------|
| GET    | `/api/rooms/`        | Listar salas                       |
| POST   | `/api/rooms/`        | Crear sala (admin con token)       |
| PUT    | `/api/rooms/{id}/`   | Reemplazar sala (admin con token)  |
| PATCH  | `/api/rooms/{id}/`   | Editar sala (admin con token)      |
| DELETE | `/api/rooms/{id}/`   | Eliminar sala (admin con token)    |

---


## 📝 Frontend

- Página inicial (`/`) para ingresar nombre de usuario y seleccionar una sala.
- Vista tipo chat estilo WhatsApp: mensajes alineados a izquierda/derecha, con colores distintos.

---

## 🔐 Seguridad WebSocket

- El `username` se guarda en `localStorage` y se envía como primer mensaje WebSocket (`type: "init"`).
- El backend valida que el nombre no esté duplicado en la misma sala.
- Las conexiones sin username válido o a salas inexistentes se rechazan.

---

## ✨ Autor

Rodrigo Maffei.

[Github](https://www.github.com/ramaffei)

[Linkedin](https://www.linkedin.com/in/ramaffei)