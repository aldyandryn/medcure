from django.shortcuts import *
from main.models import *
from django.http import *
from main.forms import *
from django.urls import *
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
     # Menggunakan .get() untuk menghindari KeyError
    last_login = request.COOKIES.get('last_login', 'Belum Pernah Login')

    context = {
        'name': request.user.username,
        'class': 'PBP B', # Kelas PBP kamu
        'items': items,
        'last_login': last_login,
    }

    return render(request, "main.html", context)
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        messages.success(request, 'Item successfully added!')
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_product.html", context)
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
def increase_amount(request, id):
    item = get_object_or_404(Item, pk=id, user=request.user)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))
def decrease_amount(request, id):
    item = get_object_or_404(Item, pk=id, user=request.user)
    if item.amount > 0:  # Ensure the amount doesn't go negative
        item.amount -= 1
        item.save()
    else: 
        messages.info(request, f'Jumlah sudah 0, tidak bisa dikurangi lagi!')
    return HttpResponseRedirect(reverse('main:show_main'))
def remove_item(request, id):
    item = get_object_or_404(Item, pk=id, user=request.user)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
def get_product_json(request):
    item_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item_item))

@csrf_exempt
def create_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        price = request.POST.get("price")
        user = request.user

        new_item = Item(name=name, amount=amount,description=description,price=price,user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
