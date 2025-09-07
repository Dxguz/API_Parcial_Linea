from django.urls import path
from .views import (
    AutorListCreateView, AutorDetailView,
    EditorialListCreateView, EditorialDetailView,
    LibroListCreateView, LibroDetailView,
    MiembroListCreateView, MiembroDetailView,
    PrestamoListCreateView, PrestamoDetailView,
)

urlpatterns = [
    # Autores
    path("autores/", AutorListCreateView.as_view(), name="autor-list"),
    path("autores/<int:pk>/", AutorDetailView.as_view(), name="autor-detail"),

    # Editoriales
    path("editoriales/", EditorialListCreateView.as_view(), name="editorial-list"),
    path("editoriales/<int:pk>/", EditorialDetailView.as_view(), name="editorial-detail"),

    # Libros
    path("libros/", LibroListCreateView.as_view(), name="libro-list"),
    path("libros/<int:pk>/", LibroDetailView.as_view(), name="libro-detail"),

    # Miembros
    path("miembros/", MiembroListCreateView.as_view(), name="miembro-list"),
    path("miembros/<int:pk>/", MiembroDetailView.as_view(), name="miembro-detail"),

    # Préstamos
    path("prestamos/", PrestamoListCreateView.as_view(), name="prestamo-list"),
    path("prestamos/<int:pk>/", PrestamoDetailView.as_view(), name="prestamo-detail"),
]