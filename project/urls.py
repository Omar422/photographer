"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic.base import RedirectView
from home.views import home_page
from service.views import (
    categories_list,
    category_details
)

urlpatterns = [
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # path('', RedirectView.as_view(url='portfolio')),
    path('', home_page, name='home'),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('services/', include('service.urls', namespace='services')),
    path('cart/', include('order.urls', namespace='orders')),
    path('categories', categories_list, name='categories'),
    path('categories/<slug:categoryURL>', category_details, name='category_details')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)