from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    detalle=models.TextField()
    imagen=models.ImageField(upload_to="projects",verbose_name="Imagen")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
class Replica(models.Model):
    nombre=models.CharField(max_length=30)
    detalle=models.TextField()
    numero=models.SmallIntegerField() # un entero pequeño
    vof=models.BooleanField()
    class Meta:
        verbose_name = "Réplica"
        verbose_name_plural = "Réplicas"


    def __str__(self):
        return self.nombre
    

