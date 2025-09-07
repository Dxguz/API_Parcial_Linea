from django.db import models


#MODELO AUTOR 1
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True, editable=False, db_column='T001IdPersona')
    nombre = models.CharField(max_length=100, db_column='T001Nombre')
    apellido = models.CharField(max_length=100, db_column='T001Apellido')
    biografia = models.TextField(db_column='T001Biografia')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'T001Autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
        

#MODELO EDITORIAL 2
class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True, editable=False, db_column='T002IdEditorial')
    nombre = models.CharField(max_length=100, db_column='T002Nombre')
    direccion = models.CharField(max_length=100, db_column='T002Direccion')
    telefono = models.CharField(max_length=100, db_column='T002Telefono')

    def __str__(self):
        return f"{self.nombre} {self.direccion} {self.telefono}"

    class Meta:
        db_table = 'T002Editorial'
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

#MODELO LIBRO 3       
class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True, editable=False, db_column='T003IdLibro')
    titulo = models.CharField(max_length=100, db_column='T003Titulo')
    resumen = models.TextField(db_column='T003Resumen')
    isbn = models.CharField(max_length=100, db_column='T003ISBN', unique=True)
    anio_publicacion = models.PositiveIntegerField(db_column='T003AnioPublic', default=0) #Para guardar solo el año y no la fecha completa
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros', db_column='T003AutorId')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libros', db_column='T003EditorialId')
    
    def __str__(self):
        return f"{self.titulo} - {self.isbn} - {self.autor}"

    class Meta:
        db_table = 'T003Libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

#MODELO MIEMBRO 4
class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True, editable=False, db_column='T004IdMiembro')
    nombre = models.CharField(max_length=100, db_column='T004Nombre')
    apellido = models.CharField(max_length=100, db_column='T004Apellido')
    email = models.EmailField(max_length=100, db_column='T004Email')
    fecha_membresia = models.DateField(db_column='T004FechaMembresia')

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"

    class Meta:
        db_table = 'T004Miembro'
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'
        
#MODELO PRESTAMO 5
class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True, editable=False, db_column='T005IdPrestamo')
    fecha_prestamo = models.DateField(db_column='T005FechaPrestamo')
    fecha_devolucion = models.DateField(db_column='T005FechaDevolucion', null=True, blank=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos', db_column='T005LibroId')
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='prestamos', db_column='T005MiembroId')
    

    def __str__(self):
        return f"{self.libro} prestado a {self.miembro}"

    class Meta:
        db_table = 'T005Prestamo'
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        