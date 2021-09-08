from django.urls import path
from .import views

urlpatterns = [
    path('iniciarSesion', views.inciarSesion, name="iniciar"),
    path('', views.loginPage, name="login"),
    path('registrar_usuario/', views.registrar_usuario, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('lista/', views.lista_producto, name="productos"),
    path('add_producto/', views.agregar_producto, name="add_prod"),

  
]