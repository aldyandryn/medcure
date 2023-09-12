from django.shortcuts import render
from main.models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    return render(request, 'main.html', {'products': products})