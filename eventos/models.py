from __future__ import unicode_literals
from django.db import models	

# Create your models here.

class User(models.Model):
	#atributos
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	nombreUser = models.CharField(max_length=100)
	correo = models.CharField(max_length=100)
	password = models.CharField(max_length=40)

	def __str__(self):
		return self.nombre


class Venue(models.Model):

	#atributos
	nombre = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='venues-img', blank=False)

	#direccion
	calle = models.CharField(max_length=100)
	numero = models.IntegerField()
	numeroInt =  models.CharField(max_length=9, blank=True)
	colonia = models.CharField(max_length=100)
	codigoPostal = models.CharField(max_length=15)
	ciudad = models.CharField(max_length=40)
	estado = models.CharField(max_length=40)
	pais = models.CharField(max_length=50, blank=False)

	capacidadPersonas = models.IntegerField()
	precio = models.IntegerField()
	monedaCambio = models.CharField(max_length=30)

	numeroAsientos = models.IntegerField(blank=True)	
	seccion = models.BooleanField()

	def __str__(self):
		return self.nombre

class Seccion(models.Model):
	#atributos
	nombreSeccion = models.CharField(max_length=6)
	numeroAsientosSeccion = models.IntegerField(blank=True)
	costoSeccion = models.IntegerField(blank=False)
	venue = models.ForeignKey(Venue, related_name='venueSecciones')
	
	def __str__(self):
		return self.nombreSeccion

class Artista(models.Model):
	#atributos
	nombre = models.CharField(max_length=100)
	nacionalidad = models.CharField(max_length=20)
	costo = models.IntegerField()
	monedaCambio = models.CharField(max_length=20)
	integrantes = models.IntegerField()
	espectadores = models.IntegerField()
	asistentesPorConcierto = models.IntegerField()
	discoReciente = models.BooleanField()
	imagen = models.ImageField(upload_to='artist-img', blank=False)


	def __str__(self):
		return self.nombre

class Evento(models.Model):
	#atributos
	venue = models.ForeignKey(Venue, related_name='venueEvento')
	fecha = models.DateTimeField(blank=False)
	artista = models.ForeignKey(Artista, related_name='artistaEvento')

	def __str__(self):
		return self.artista+'en'+self.venue


