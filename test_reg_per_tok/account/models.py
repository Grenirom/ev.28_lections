from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.managers import MyManager


class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField(_('first_name'), max_length=50)
    last_name = models.CharField(_('last_name'), max_length=50)
    activation_code = models.CharField(max_length=250, blank=True)
    username = models.CharField(max_length=50, unique=True)
    avatar = models.ImageField(upload_to='images/', blank=True, default_avatar='images/default_avatar.jpg')
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = MyManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    def create_activation_code(self):
        code = str(uuid4())
        self.activation_code = code
