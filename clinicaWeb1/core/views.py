
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ProductoForm, CustomUserForm

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def inscripcion(request):
    return render(request, 'core/inscripcion.html')

def productos(request):
    return render(request, 'core/productos.html')


def quienessomos(request):
    return render(request, 'core/quienessomos.html')


def Lista_Producto(request):
    producto = Producto.objects.all()
    data = {
        'producto':producto
    }
    return render(request, 'core/Lista_Producto.html', data)

@login_required
def aniadir_producto(request):
    data = {
        'form':ProductoForm()
    }

    if request.method =='POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado con exito"

    return render(request, 'core/aniadir_producto.html', data)


@login_required
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado con exito"
            return redirect(to="Lista_Producto")
        data['form'] = formulario
    return render(request, 'core/modificar_producto.html', data)


@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="Lista_Producto")


def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save();
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect(to='home')


    return render(request, "registration/registrar.html", data)