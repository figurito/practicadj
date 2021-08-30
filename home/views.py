from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Producto
from .forms import Productos_Form
from django.contrib import messages

def register(request):
    context ={}
    return render(request, 'register.html', context)

def login(request):
    context ={}
    return render(request, 'login_page.html', context)

def lista_producto(request):
    producto = Producto.objects.all()
    context = {'productos':producto}
    return render(request, 'lista_productos.html', context)

def agregar_producto(request):
    form = Productos_Form()
    context={'form':form}
    return render(request, 'agregar_producto.html', context)











'''def login(request):
    usu=''
    cla=''
    if request.method == "POST":
            formulario = login_form(request.POST)
            if formulario.is_valid():
                usu=formulario.cleaned_data['usuario']
                cla=formulario.cleaned_data['clave']
                usuario=authenticate(username=usu, password=cla)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return redirect('/')
                else:
                    msj= 'Usuario o Clave Incorrectos'
    formulario=login_form()
    return render(request, 'login.html', {'form':formulario})'''

'''def login(request):
	if request.user.is_authenticated:
		return redirect('login')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('login')
			else:
				messages.info(request, 'Usuario o Clave Incorrecta')

		context = {}
		return render(request, 'login.html', context)
'''

def carrito_compra(request):
    producto = Producto.objects.all()
    context = {'productos':producto}
    return render(request, 'lista_productos.html', context)
