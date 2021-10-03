from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Order
from .forms import AddOrder
from service.models import Service


# Create your views here.

@login_required(login_url='/accounts/login/')
def orders_list(request):
    total_price = 0
    try:
        orders = Order.objects.filter(order_user = request.user)
        total_price = sum([order.order_service.service_price for order in orders])
        # for order in orders:
        #     service_price = order.order_service.service_price
        #     total_price += service_price
                
    except Exception as e:
        orders = False
        print(e)
    
    return render(request, 'order/index.html', {
        'orders'        : orders,
        'total_price'   : total_price})


@login_required(login_url='/accounts/login/')
def add_order(request, orderURL):

    service = Service.objects.get(service_slug = orderURL)
    
    if request.method == 'POST':
        add_order = AddOrder(request.POST)
        if add_order.is_valid():
            form = add_order.save(commit=False)
            form.order_user = request.user
            form.order_service = service
            form.save()
            return redirect(reverse('orders:order_list'))
    else:
        add_order = AddOrder()
    
    return render(request, 'order/add_order.html', {
        'add_order' : add_order,
        'service'   : service
        })


@login_required(login_url='/accounts/login/')
def delete_order(request, orderId):
    order = Order.objects.get(id = orderId).delete()
    # order.delete()
    return redirect(reverse('orders:order_list'))