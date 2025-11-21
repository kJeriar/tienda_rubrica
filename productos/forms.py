from django import forms
from django.core.validators import MinValueValidator
from .models import Producto, Categoria, Etiqueta, Detalle

# ---------- PRODUCTO ----------
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'   # nombre, descripción, precio, categoría, etiquetas, detalle

    # Validación extra (opcional)
    precio = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        widget=forms.NumberInput(attrs={'step': '0.01', 'min': '0'})
    )


# ---------- CATEGORIA ----------
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


# ---------- ETIQUETA ----------
class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']


# ---------- DETALLE ----------
class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ['dimensiones', 'peso']