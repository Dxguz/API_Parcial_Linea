from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import (
    AutorSerializer,
    EditorialSerializer,
    LibroSerializer,
    MiembroSerializer,
    PrestamoSerializer,
)


#   AUTOR
class AutorListCreateView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def get(self, request):
        autores = Autor.objects.all()
        if not autores:
            raise NotFound("No se encontraron autores.")
        serializer = AutorSerializer(autores, many=True)
        return Response({"success": True, "detail": "Listado de autores.", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AutorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "detail": "Autor creado correctamente.", "data": serializer.data}, status=status.HTTP_201_CREATED)


class AutorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def get(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        serializer = AutorSerializer(autor)
        return Response({"success": True, "detail": "Autor encontrado.", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        serializer = AutorSerializer(autor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "detail": "Autor actualizado correctamente.", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        autor.delete()
        return Response({"success": True, "detail": "Autor eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)


#   EDITORIAL
class EditorialListCreateView(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def get(self, request):
        editoriales = Editorial.objects.all()
        if not editoriales:
            raise NotFound("No se encontraron editoriales.")
        serializer = EditorialSerializer(editoriales, many=True)
        return Response({"success": True, "detail": "Listado de editoriales.", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EditorialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "detail": "Editorial creada correctamente.", "data": serializer.data}, status=status.HTTP_201_CREATED)


class EditorialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def get(self, request, pk):
        editorial = get_object_or_404(Editorial, pk=pk)
        serializer = EditorialSerializer(editorial)
        return Response({"success": True, "detail": "Editorial encontrada.", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        editorial = get_object_or_404(Editorial, pk=pk)
        serializer = EditorialSerializer(editorial, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "detail": "Editorial actualizada correctamente.", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        editorial = get_object_or_404(Editorial, pk=pk)
        editorial.delete()
        return Response({"success": True, "detail": "Editorial eliminada correctamente."}, status=status.HTTP_204_NO_CONTENT)


#   LIBRO
class LibroListCreateView(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request):
        libros = Libro.objects.all()
        autor_id = request.query_params.get("autor")
        editorial_id = request.query_params.get("editorial")

        if autor_id:
            libros = libros.filter(autor__id_autor=autor_id)
        if editorial_id:
            libros = libros.filter(editorial__id_editorial=editorial_id)

        if not libros:
            raise NotFound("No se encontraron libros.")
        serializer = LibroSerializer(libros, many=True)
        return Response({"success": True, "detail": "Listado de libros.", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LibroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "detail": "Libro creado correctamente.", "data": serializer.data}, status=status.HTTP_201_CREATED)


class LibroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        serializer = LibroSerializer(libro)
        return Response({"success": True, "detail": "Libro encontrado.", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        serializer = LibroSerializer(libro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "detail": "Libro actualizado correctamente.", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        libro.delete()
        return Response({"success": True, "detail": "Libro eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)


#   MIEMBRO
class MiembroListCreateView(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def get(self, request):
        miembros = Miembro.objects.all()
        if not miembros:
            raise NotFound("No se encontraron miembros.")
        serializer = MiembroSerializer(miembros, many=True)
        return Response({"success": True, "detail": "Listado de miembros.", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MiembroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "detail": "Miembro creado correctamente.", "data": serializer.data}, status=status.HTTP_201_CREATED)


class MiembroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def get(self, request, pk):
        miembro = get_object_or_404(Miembro, pk=pk)
        serializer = MiembroSerializer(miembro)
        return Response({"success": True, "detail": "Miembro encontrado.", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        miembro = get_object_or_404(Miembro, pk=pk)
        serializer = MiembroSerializer(miembro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "detail": "Miembro actualizado correctamente.", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        miembro = get_object_or_404(Miembro, pk=pk)
        miembro.delete()
        return Response({"success": True, "detail": "Miembro eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)


#   PRESTAMO
class PrestamoListCreateView(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get(self, request):
        prestamos = Prestamo.objects.all()
        miembro_id = request.query_params.get("miembro")
        fecha = request.query_params.get("fecha_prestamo")

        if miembro_id:
            prestamos = prestamos.filter(miembro__id_miembro=miembro_id)
        if fecha:
            prestamos = prestamos.filter(fecha_prestamo=fecha)

        if not prestamos:
            raise NotFound("No se encontraron préstamos.")
        serializer = PrestamoSerializer(prestamos, many=True)
        return Response({"success": True, "detail": "Listado de préstamos.", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PrestamoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "detail": "Préstamo creado correctamente.", "data": serializer.data}, status=status.HTTP_201_CREATED)


class PrestamoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        serializer = PrestamoSerializer(prestamo)
        return Response({"success": True, "detail": "Préstamo encontrado.", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        serializer = PrestamoSerializer(prestamo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "detail": "Préstamo actualizado correctamente.", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        prestamo.delete()
        return Response({"success": True, "detail": "Préstamo eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
