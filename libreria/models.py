from django.db import models

# Create your models here.
class Pelicula(models.Model):
    # pongo el id aunque no es necesario
    # el problema que no me insertaba registros era que yo hacía los inserts forzando los ids
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nombre_ingles = models.CharField(max_length=100, default="", blank=True, null=True)
    nombre_alternativo = models.CharField(max_length=100, default="", blank=True, null=True)
    anio = models.IntegerField(verbose_name="Año")
    imagen = models.CharField(max_length=50, verbose_name="Imagen", default="", blank=True, null=True)
    director = models.CharField(max_length=100, default="")
    actor_1 = models.CharField(max_length=100, default="", blank=True, null=True)
    actor_2 = models.CharField(max_length=100, default="", blank=True, null=True)
    actor_3 = models.CharField(max_length=100, default="", blank=True, null=True)
    actor_4 = models.CharField(max_length=100, default="", blank=True, null=True)
    actor_5 = models.CharField(max_length=100, default="", blank=True, null=True)
    actor_6 = models.CharField(max_length=100, default="", blank=True, null=True)
    pais = models.CharField(max_length=40, default="", blank=True, null=True)
    imdb = models.CharField(max_length=100, default="", blank=True, null=True)
    resenia = models.TextField(verbose_name="Reseña", blank=True, default="", null=True)
    top10 = models.BooleanField(verbose_name="Top", default=False, null=True)
    imagenlocal = models.ImageField(upload_to='imagenes/', verbose_name="ImagenLocal", null=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.nombre + " (" + str(self.anio) + ", " + self.director + ")"
        return fila

    # En el caso que tuviera una imagen guardada (versión anterior)
    #def delete(self, using=True, keep_parents=False):
    #    self.imagen.storage.delete(self.imagen.name)
    #    super().delete()


