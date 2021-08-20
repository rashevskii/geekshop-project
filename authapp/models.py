from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expired = models.DateTimeField(default=now() + timedelta(hours=48))

    class Meta:
        ordering = '-is_active', '-is_superuser', '-is_staff', 'username'

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expired:
            return False
        else:
            return True
