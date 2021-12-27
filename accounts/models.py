from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('المستخدم'), related_name='user_id')
    user_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name=_('الجوال'))
    user_address = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('العنوان'))
    user_slug = models.SlugField(verbose_name=_("الرابط"), blank=True, null=True)

    def save(self, *args, **kwargs):
        self.user_slug = slugify(self.user.username, allow_unicode=True)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )