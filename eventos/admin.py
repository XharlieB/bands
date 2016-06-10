from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Venue)
admin.site.register(models.Seccion)
admin.site.register(models.Artista)
admin.site.register(models.Evento)
admin.site.register(models.User)