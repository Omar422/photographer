from django.shortcuts import render
from .models import Service, Category

# Create your views here.
def services_list(request):
    services_list = Service.objects.all()
    return render(request, 'service/index.html', {'services':services_list})


def service_details(request, serviceURL):
    service_details = Service.objects.get(service_slug = serviceURL)
    return render(request, 'service/details.html', {'details':service_details})


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