from django.shortcuts import render
from .models import Slider, Partner

def home_page(request):

    partners = Partner.objects.all()
    images = Slider.objects.filter(slider_active=True)
    imgs_len = [i for i in range(len(images))]
    
    return render(request, 'home/index.html', {
        'partners'  :   partners,
        'images'    :   images,
        'imgs_len'  :   imgs_len,
    })