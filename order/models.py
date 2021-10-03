from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


ORDER_STATUS = (
    (_("underway"), _("underway")),
    (_("confirmed"), _("confirmed")),
    (_("completed"), _("completed"))
)

class Order(models.Model):
    order_user = models.ForeignKey(User, verbose_name=_("User"), related_name="user", on_delete=models.CASCADE)
    order_service = models.ForeignKey("service.Service", verbose_name=_("Service"), related_name="service", on_delete=models.CASCADE)
    order_status = models.CharField(verbose_name = _("Status"), max_length=15, choices=ORDER_STATUS, default="underway")
    order_date_service = models.DateField(verbose_name= _("Service Date"), auto_now=False, auto_now_add=False, blank=True)
    order_date_request = models.DateTimeField(verbose_name= _("Order Date"), auto_now_add=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"user: {self.order_user.username} --- order: {self.order_service.service_name}"