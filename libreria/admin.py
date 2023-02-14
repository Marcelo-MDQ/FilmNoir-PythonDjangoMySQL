from django.contrib import admin
from .models import Pelicula
from .models import Actor
from .models import Director

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Actor)
admin.site.register(Director)