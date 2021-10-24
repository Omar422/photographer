from django.db import models
from django.utils.translation import ugettext as _

class Slider(models.Model):

	slider_image = models.ImageField(upload_to='slider/', verbose_name=_("الصورة"))
	slider_active = models.BooleanField(default=False, verbose_name=_("إظهار الصورة"))

	class Meta:
		verbose_name = _("صورة")
		verbose_name_plural = _("صور الشرائح")

	def __str__(self):
		return str(self.slider_image)


class Partner(models.Model):

	partner_name = models.CharField(max_length=50, verbose_name=_("الاسم"))
	partner_image = models.ImageField(verbose_name=_("الصورة"), upload_to='partner/')
	partner_event = models.CharField(max_length=200, verbose_name=_("رابط التغطية"), blank=True, null=True)

	class Meta:
		verbose_name = _("شريك نجاح")
		verbose_name_plural = _("شركاء النجاح")

	def __str__(self):
		return self.partner_name