from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import slugify

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=250, verbose_name=_("الاسم"))
    service_description = models.TextField(verbose_name=_("الوصف"))
    service_price = models.DecimalField(verbose_name=_("السعر"), max_digits=5, decimal_places=2)
    service_category = models.ForeignKey("Category", verbose_name=_("القسم"), on_delete=models.CASCADE)
    service_image = models.ImageField(upload_to="service/", verbose_name=_("الصورة"), blank=True, null=True)
    service_slug = models.SlugField(verbose_name = _("الرابط"), blank=True, null=True, allow_unicode=True)

    class Meta:
        verbose_name = _("خدمة")
        verbose_name_plural = _("الخدمات")

    def save(self, *args, **kwargs):
        self.service_slug = slugify(self.service_name)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.service_name

class Category(models.Model):
    category_name = models.CharField(verbose_name=_("القسم"), max_length=50)
    category_description = models.TextField(verbose_name=_("الوصف"))
    category_image = models.ImageField(verbose_name=_("الصورة"), upload_to="category/", blank=True, null=True)
    category_slug = models.SlugField(verbose_name=_("الرابط"), blank=True, null=True)

    class Meta:
        verbose_name = _("قسم")
        verbose_name_plural = _("الأقسام")

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name