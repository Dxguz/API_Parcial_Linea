from rest_framework import serializers
from .models import Autor, Editorial, Libro, Miembro, Prestamo


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = "__all__"


class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.CharField(source="autor.nombre", read_only=True)
    autor_apellido = serializers.CharField(source="autor.apellido", read_only=True)
    editorial_nombre = serializers.CharField(source="editorial.nombre", read_only=True)

    class Meta:
        model = Libro
        fields = "__all__"


class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = "__all__"


class PrestamoSerializer(serializers.ModelSerializer):
    libro_titulo = serializers.CharField(source="libro.titulo", read_only=True)
    miembro_nombre = serializers.CharField(source="miembro.nombre", read_only=True)
    miembro_apellido = serializers.CharField(source="miembro.apellido", read_only=True)

    class Meta:
        model = Prestamo
        fields = "__all__"