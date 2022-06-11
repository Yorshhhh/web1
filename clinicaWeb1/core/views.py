from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def inscripcion(request):
    return render(request, 'core/inscripcion.html')

def productos(request):
    return render(request, 'core/productos.html')

def quienessomos(request):
    return render(request, 'core/quienessomos.html')