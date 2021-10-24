from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Order, ORDER_STATUS


# Create your views here.

@login_required(login_url='/accounts/login/')
def orders_list(request):
    total_price = 0
    try:
        orders = Order.objects.filter(order_user = request.user)
        total_price = sum([order.order_service.service_price for order in orders])
                
    except Exception as e:
        orders = False
    
    return render(request, 'order/index.html', {
        'orders'        : orders,
        'total_price'   : total_price,
        'status'        : dict(ORDER_STATUS).items()})



@login_required(login_url='/accounts/login/')
def delete_order(request, orderId):
    order = Order.objects.get(id = orderId).delete()
    # order.delete()
    return redirect(reverse('orders:order_list'))