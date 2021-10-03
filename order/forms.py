from django.forms import ModelForm, DateInput
from .models import Order
import datetime

# class MyDate(DateInput):
#     input_type = 'date'
# 'order_date_service' : MyDate(attrs={'required':'required'})

class AddOrder(ModelForm):
    class Meta:
        model = Order
        fields = ['order_date_service']
        widgets = {
            'order_date_service' : DateInput(
                attrs = {
                    'type' : 'date',
                    'required': 'required',
                    'min': datetime.date.today() + datetime.timedelta(days=2)
                }
            )
        }