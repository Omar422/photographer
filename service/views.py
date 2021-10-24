from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Service, Category
from django.contrib.auth.decorators import login_required
from order.forms import AddOrder


def categories_list(request):
    categories_list = Category.objects.all()
    return render(request, 'category/index.html', {'categories':categories_list})


def category_details(request, categoryURL):
    category_details = Category.objects.get(category_slug = categoryURL)
    # category_services = Service.objects.filter(service_category = category_details.id)
    category_services = category_details.service_set.all()
    return render(request, 'category/details.html',{
        'details': category_details,
        'services': category_services
        })


def services_list(request):
    services_list = Service.objects.all()
    return render(request, 'service/index.html', {'services':services_list})


@login_required(login_url='/accounts/login/')
def service_details(request, serviceURL):
    service_details = Service.objects.get(service_slug = serviceURL)
    print(f'service: {service_details}')

    if request.method == 'POST':
        add_order = AddOrder(request.POST)
        if add_order.is_valid():
            form = add_order.save(commit=False)
            form.order_user = request.user
            form.order_service = service_details
            form.save()
            return redirect(reverse('orders:order_list'))
    else:
        add_order = AddOrder()

    # return render(request, 'service/details.html', {'details':service_details})
    return render(request, 'service/confirm.html', {
        'details'       :   service_details,
        'add_order'     :   add_order,
        })