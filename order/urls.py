from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.orders_list, name='order_list'),
    path('delete_order/<slug:orderId>', views.delete_order, name='delete_order'),
]
