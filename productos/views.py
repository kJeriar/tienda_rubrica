from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Categoria, Etiqueta
from .forms import ProductoForm, CategoriaForm, EtiquetaForm

# ---------- INDEX ----------
def index(request):
    return render(request, 'index.html')

# ---------- PRODUCTOS ----------
@login_required
def lista_productos(request):
    qs = Producto.objects.select_related('categoria').prefetch_related('etiquetas')
    
    # Depuración (opcional)
    print("=== FILTROS ===")
    print("Total antes:", qs.count())
    
    # Buscador por nombre
    query = request.GET.get('q')
    if query:
        qs = qs.filter(nombre__icontains=query)
        print("Después de nombre:", qs.count())
    
    # Filtro por categoría
    categoria_id = request.GET.get('categoria')
    print("Categoría recibida (raw):", categoria_id)

    categoria_id_int = None
    if categoria_id:
        try:
            categoria_id_int = int(categoria_id)
            qs = qs.filter(categoria_id=categoria_id_int)
            print("Después de categoría:", qs.count())
        except ValueError:
            print("Valor de categoría inválido:", categoria_id)
    
    # Ordenamiento
    orden = request.GET.get('orden', 'nombre')
    if orden == 'precio':
        qs = qs.order_by('-precio')
    else:
        qs = qs.order_by('nombre')
    
    print("Final:", qs.count())
    
    # Siempre pasar categorías para el select
    categorias = Categoria.objects.all()
    
    return render(request, 'lista_productos.html', {
        'productos': qs,
        'query': query,
        'categoria_id': categoria_id,
        'categorias': categorias,
        'orden': orden,
    })
@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

# ---------- CATEGORÍAS ----------
@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

@login_required
def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_categorias')
    return render(request, 'formulario_categoria.html', {'form': form})

@login_required
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('lista_categorias')
    return render(request, 'formulario_categoria.html', {'form': form})

@login_required
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'eliminar_categoria.html', {'categoria': categoria})

# ---------- ETIQUETAS ----------
@login_required
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'lista_etiquetas.html', {'etiquetas': etiquetas})

@login_required
def crear_etiqueta(request):
    form = EtiquetaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_etiquetas')
    return render(request, 'formulario_etiqueta.html', {'form': form})

@login_required
def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    form = EtiquetaForm(request.POST or None, instance=etiqueta)
    if form.is_valid():
        form.save()
        return redirect('lista_etiquetas')
    return render(request, 'formulario_etiqueta.html', {'form': etiqueta})

@login_required
def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')
    return render(request, 'eliminar_etiqueta.html', {'etiqueta': etiqueta})