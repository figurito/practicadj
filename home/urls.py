from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('', views.lista_producto, name="productos"),
    path('add_producto/', views.agregar_producto, name="add_prod"),
    path('logout/', views.logout, name="logout"),
    path('cart/', views.carrito_compra, name="cart"),
]