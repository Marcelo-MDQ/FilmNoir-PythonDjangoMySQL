from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Pelicula
from .models import Actor
from .models import Director
from .forms import PeliculaForm

# Create your views here.
def inicio(request):
    peliculas = Pelicula.objects.all().order_by('-id')[:3]
    return render(request, 'paginas/inicio.html', {'peliculas': peliculas})

def registro(request):

    if request.method == 'GET':
        return render(request, 'paginas/registro.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio')
            except:
                return render(request, 'paginas/registro.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
                
        return render(request, 'paginas/registro.html', {
                    'form': UserCreationForm,
                    "error": 'Las passwords no coinciden'
                })

def iniciarsesion(request):
    if request.method == 'GET':
        return render(request, 'paginas/iniciarsesion.html', {
            'form': AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'paginas/iniciarsesion.html', {
                'form': AuthenticationForm,
                "error": 'Usuario o password incorrecto'
             })
        else:
            login(request, user)
            return redirect('inicio')

def cerrarsesion(request):
    logout(request)
    return redirect('inicio')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def queeselfilmnoir(request):
    return render(request, 'paginas/queeselfilmnoir.html')
    
def buscador(request):
    peliculas = []
    queryset = request.GET.get("buscar")
    if queryset:
        peliculas = (Pelicula.objects.filter(nombre__icontains=queryset).all() | 
            Pelicula.objects.filter(director__icontains=queryset) | 
            Pelicula.objects.filter(actor_1__icontains=queryset).all() | 
            Pelicula.objects.filter(actor_2__icontains=queryset).all() | 
            Pelicula.objects.filter(actor_3__icontains=queryset).all() | 
            Pelicula.objects.filter(actor_4__icontains=queryset).all() | 
            Pelicula.objects.filter(actor_5__icontains=queryset).all() | 
            Pelicula.objects.filter(actor_6__icontains=queryset).all()).order_by('anio', 'nombre')    
    
    return render(request, 'paginas/buscador.html', {'peliculas': peliculas, 'buscador': queryset})

@login_required
def abmpeliculas(request):
    peliculas = Pelicula.objects.all().order_by('id')
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})

def peliculas(request):
    peliculas = Pelicula.objects.all().order_by('nombre')
    return render(request, 'paginas/peliculas.html', {'peliculas': peliculas})

def peliculascajitas(request):
    peliculas = Pelicula.objects.all().order_by('anio', 'nombre')
    return render(request, 'paginas/peliculas-cajitas.html', {'peliculas': peliculas})

def peliculasxordenresenia(request):
    peliculas = Pelicula.objects.all().order_by('id')
    return render(request, 'paginas/peliculasxordenresenia.html', {'peliculas': peliculas})

def top10(request):
    peliculas = Pelicula.objects.filter(top10=True).all()
    return render(request, 'paginas/top10.html', {'peliculas': peliculas})

def actores(request):
    actores = []
    peliculas = Pelicula.objects.all()
    for pelicula in peliculas:
        actor = pelicula.actor_1
        if actor:
            if actor not in actores:
                actores.append(actor)

        actor = pelicula.actor_2
        if actor:
            if actor not in actores:
                actores.append(actor)

        actor = pelicula.actor_3
        if actor:
            if actor not in actores:
                actores.append(actor)

        actor = pelicula.actor_4
        if actor:
            if actor not in actores:
                actores.append(actor)

        actor = pelicula.actor_5
        if actor:
            if actor not in actores:
                actores.append(actor)

        actor = pelicula.actor_6
        if actor:
            if actor not in actores:
                actores.append(actor)

    actores.sort()
    return render(request, 'paginas/actores.html', {'actores': actores})

def directores(request):
    directores = []
    peliculas = Pelicula.objects.all()
    for pelicula in peliculas:
        director = pelicula.director
        if director not in directores:
            directores.append(director)
    directores.sort()
    return render(request, 'paginas/directores.html', {'directores': directores})

def crear(request):
    formulario = PeliculaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('peliculas')
    return render(request, 'peliculas/crear.html', {'formulario': formulario})

def editar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    formulario = PeliculaForm(request.POST or None, request.FILES or None, instance=pelicula)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('peliculas')
    return render(request, 'peliculas/editar.html', {'formulario': formulario})

def buscar(request, aBuscar):
    peliculas = Pelicula.objects.filter(nombre__icontains=aBuscar).all().order_by('anio', 'nombre')
    return render(request, 'peliculas/mostrar.html', {'peliculas': peliculas})

def buscarDirector(request, director):
    peliculas = []
    peliculas = Pelicula.objects.filter(director=director).all().order_by('anio', 'nombre')

    directores = []
    directores = Director.objects.filter(nombredirector=director).all() 
    return render(request, 'paginas/buscador.html', {'peliculas': peliculas, 'director': director, 'directores': directores})

def buscarActor(request, actor):
    peliculas = []
    peliculas = (Pelicula.objects.filter(actor_1=actor).all() | 
    Pelicula.objects.filter(actor_2=actor).all() | 
    Pelicula.objects.filter(actor_3=actor).all() | 
    Pelicula.objects.filter(actor_4=actor).all() | 
    Pelicula.objects.filter(actor_5=actor).all() | 
    Pelicula.objects.filter(actor_6=actor).all()).order_by('anio', 'nombre')

    actores = []
    actores = Actor.objects.filter(nombreactor=actor).all() 
    return render(request, 'paginas/buscador.html', {'peliculas': peliculas, 'actor': actor, 'actores': actores})

def eliminar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('peliculas')

def reseniaPelicula(request, id):
    peliculas = Pelicula.objects.get(id=id)
    return render(request, 'paginas/reseniaPelicula.html', {'peliculas': peliculas})
