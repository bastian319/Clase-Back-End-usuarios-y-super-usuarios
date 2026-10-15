from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Comprobar si el usuario es administrador
def es_administrador(user):
    return user.is_authenticated and (user.is_superuser or user.group.filter(name='Administrador').exists())

# Comprueba que pertenece al grupo de usuarios
def es_usuario(user):
    return user.is_authenticated and (user.is_superuser or user.group.filter(name='Usuario').exists())

# Comprueba si pertenece al grupo de invitados
def es_invitado(user):
    return user.is_authenticated and (user.is_superuser or user.group.filter(name='Invitado').exists())

#

# Create your views here.
@login_required
def index(request):
    return render (request, 'index.html')

@login_required
@user_passes_test(es_invitado)
def invitados(request):
    return render (request, 'invitados.html')

@login_required
@user_passes_test(es_usuario)
def pagina(request):
    return render (request, 'pagina.html')

@login_required
@user_passes_test(es_administrador)
def Eliminar(request):
    return render (request, 'eliminar.html')