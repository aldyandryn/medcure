from django.shortcuts import render
from main.models import Product

# Create your views here.
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi':'MedCure',
        'nama': 'Aldyandry N',
        'kelas': 'PBP-B',
    }

    return render(request, "main.html", context)