from django.db import models
from service.models import Category
from django.utils.translation import ugettext as _

# Create your models here.

class Portfolio(models.Model):

    portfolio_title = models.CharField(verbose_name=_("العنوان"), max_length=200)
    portfolio_description = models.TextField(verbose_name=_("الوصف"))
    portfolio_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name=_("التاريخ"), blank=True)
    portfolio_images = models.CharField(verbose_name=_("رابط الصور"), max_length=200, blank=True, null=True)
    portfolio_video = models.CharField(verbose_name=_("رابط المونتاج"), max_length=200, blank=True, null=True)
    portfolio_category = models.ForeignKey(Category, related_name='portfolio_category', on_delete=models.CASCADE, verbose_name=_("القسم"))

    class Meta:
        verbose_name = _("عمل")
        verbose_name_plural = _("أعمالي")

    def __str__(self):
        return self.portfolio_title