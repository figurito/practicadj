from django.forms import ModelForm
from .models import *


class Productos_Form(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

