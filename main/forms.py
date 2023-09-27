from django.forms import ModelForm
from main.models import *

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "amount", "description"]