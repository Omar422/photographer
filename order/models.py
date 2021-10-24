from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


ORDER_STATUS = [
    (_("1"), _("تحت الدراسة")),
    (_("2"), _("مؤكد")),
    (_("3"), _("منفذ"))
]

class Order(models.Model):
    order_user = models.ForeignKey(User, verbose_name=_("المسخدم"), related_name="user", on_delete=models.CASCADE)
    order_service = models.ForeignKey("service.Service", verbose_name=_("الخدمة"), related_name="service", on_delete=models.CASCADE)
    order_status = models.CharField(verbose_name = _("الحالة"), max_length=15, choices=ORDER_STATUS, default="1")
    order_date_service = models.DateField(verbose_name= _("تاريخ المناسبة"), auto_now=False, auto_now_add=False, blank=True)
    order_date_request = models.DateTimeField(verbose_name= _("تاريخ الطلب"), auto_now_add=True)

    class Meta:
        verbose_name = _("طلب")
        verbose_name_plural = _("الطلبات")

    def __str__(self):
        return self.order_user.username