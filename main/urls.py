

from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, increase_amount, decrease_amount, remove_item, get_product_json, create_item_ajax, create_product_flutter
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import logout_user



app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase/<int:id>/', increase_amount, name='increase_amount'),
    path('decrease/<int:id>/', decrease_amount, name='decrease_amount'),
    path('remove/<int:id>/', remove_item, name='remove_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/',create_item_ajax,name='create_item_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]