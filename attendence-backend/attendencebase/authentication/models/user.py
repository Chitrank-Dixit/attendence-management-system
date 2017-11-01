import random
import string
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta

# Create your models here.
from moneyed import Money
import pytz
from authentication.models.choices import GenderChoices


from miscellaneous.models import TimeStampMixin



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):
    """
        User Model for authentication and authorization purposes
    """
    username = models.CharField(max_length=60, null=True)
    first_name = models.CharField(max_length=50 ,null=True)
    last_name = models.CharField(max_length=50 ,null=True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=13, unique=True, null=True, default=None,
                              validators=[RegexValidator(regex="^\d{10}$")])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    avatar_url = models.URLField(blank=True, null=True, max_length=300)  # default max_length 200
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, null=True, blank=True)
    age = models.IntegerField(default=10, null=True, blank=True)


    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        app_label = 'authentication'

    def get_full_name(self):
        if self.first_name or self.last_name:
            full_name = self.first_name + " " + self.last_name
        else:
            full_name = "<No Name Provided>"

        return full_name

    def get_email(self):
        if self.email:
            return self.email
        return ''

    get_full_name.short_description = 'Full Name'

    def get_short_name(self):
        return self.first_name if self.first_name else " "

