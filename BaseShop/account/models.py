from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from account.manager import MyCustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_("email"), unique=True)
    password = models.CharField(_("password"), max_length=129)
    first_name = models.CharField(_("first_name"), max_length=40)
    last_name = models.CharField(_("last_name"), max_length=40)
    avatar = models.ImageField(_("avatar"), upload_to='avatars', default='default-avatar.jpg')
    username = models.CharField(_("username"), max_length=50, unique=True)
    is_active = models.BooleanField(_("is_active"), default=False)
    activation_code = models.CharField(max_length=400, blank=True)

    objects = MyCustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def create_code_to_activate(self):
        code = str(uuid4())
        self.activation_code = code