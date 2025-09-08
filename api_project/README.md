# Taller Django REST - Personas y Tareas

Este proyecto implementa una API en Django REST Framework conectada a PostgreSQL.  
La API gestiona una biblioteca con endpoints CRUD y filtros.

---

## Integrantes
- María Angélica Castro Pinzón
- Danna Ximena Guzmán Rincón

## Requisitos
- Python 3.10+
- PostgreSQL
- Django
- Django REST Framework
- Postman (para pruebas)

---

## Instalación y ejecución

# Clonar el repositorio
git clone https://github.com/Dxguz/API_Parcial_Linea.git

# Crear y activar entorno virtual
python -m venv venv
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Ejecutar servidor
python manage.py runserver

# URL documentación en Postman
https://documenter.getpostman.com/view/48127802/2sB3HnJK8Z
