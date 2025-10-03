from django.shortcuts import render

# Create your views here.
def index(request):
    productos = [
        {'nombre': 'Laptop HP Pavilion', 'precio': 899.99, 'stock': 15},
        {'nombre': 'Monitor Dell UltraSharp', 'precio': 349.00, 'stock': 22},
        {'nombre': 'Teclado Mecánico Corsair', 'precio': 129.50, 'stock': 30},
    ]
    contexto = {'productos': productos}
    return render(request, 'index.html', contexto)