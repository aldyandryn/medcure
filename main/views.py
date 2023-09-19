from django.shortcuts import *
from main.models import *
from django.http import *
from main.forms import *
from django.urls import *
from .models import Product


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Aldyandry', # Nama kamu
        'class': 'PBP B', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def delete_first_rhinos(request):
    # Cari produk "Rhinos" yang pertama
    rhinos_product = Product.objects.filter(name="Rhinos").first()
    if rhinos_product:
        rhinos_product.delete()

    # Setelah menghapus, redirect ke halaman yang diinginkan, misalnya halaman daftar produk
    return redirect('nama_url_halaman_daftar_produk')