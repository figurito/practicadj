from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import CreateUserForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm 

from django.contrib import messages

def inciarSesion(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('lista/')
            else:
                messages.info(request, 'Usuario y Contraseña Incorrecto')
                
        context = {}
        return render(request, 'iniciar.html', context)


def registrar_usuario(request):
    form= CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'registrar_usuario.html', context)





def registerPage(request):
    if request.user.is_authenticated:
        return redirect('login/')
    else:
            form = CreateUserForm()
            if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    '''username = request.POST.get('username')
                    password =request.POST.get('password1')
                    user = authenticate(request, username=username, password=password)
                    login(request, user)'''
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Cuenta Creada ' + user)
                    return redirect(to='/')

            context ={'form':form}
            return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('login/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista/')
            else:
                messages.info(request, 'Usuario y Contraseña Incorrecto')
                
        context = {}
        return render(request, 'login_page.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def lista_producto(request):
    producto = Producto.objects.all()
    context = {'productos':producto}
    return render(request, 'lista_productos.html', context)

def agregar_producto(request):
    #form = Productos_Form()
    context={}
    return render(request, 'agregar_producto.html', context)




