# Django imports
from django.db import models
from django.utils import timezone

# Model imports
from django.contrib.auth.models import AbstractBaseUser


#
# Model
#

class BaseUser(AbstractBaseUser):
    """
    """

    # User's personnal fields (REQUIRED)
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'This email address is already used by another user.'
        },
        help_text=''
    )

    phone_number = models.CharField(
        unique=True,
        max_length=16,
        error_messages={
            'unique': 'This phone number is already used by another user.',
            'max_length': ''
        },
        help_text=''
    )

    # User's location fields (REQUIRED)
    # country

    # city

    # zip_code

    address_part_1 = models.CharField(
        max_length=128,
        error_messages={
            'max_length': ''
        },
        help_text=''
    )

    address_part_2 = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        error_messages={
            'max_length': ''
        },
        help_text=''
    )

    # Account's fields
    is_active = models.BooleanField(
        default=True,
        help_text=''
    )

    registration_date = models.DateField(
        default=timezone.now,
        help_text=''
    )

    # Class settings
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'phone_number', 'address_part_1']

    @property
    def type(self):
        return "BaseUser"

    def has_perm(self, perm, obj=None):
        return False

    def has_module_perms(self, module):
        return False

    # Class properties
    @property
    def is_staff(self):
        return False

    @property
    def is_admin(self):
        return False

    # Class functions
    def get_full_address(self):
        return ""
