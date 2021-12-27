from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('<str:serviceURL>', views.service_details, name='service_details'),
]
