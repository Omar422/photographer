from django.contrib import admin

# Register your models here.
from .models import Slider, Partner

admin.site.register(Slider)
admin.site.register(Partner)