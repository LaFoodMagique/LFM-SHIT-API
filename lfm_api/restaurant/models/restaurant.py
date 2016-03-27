# Django imports
from django.db import models
from django.utils import timezone

# Model imports
from django.contrib.auth.models import AbstractBaseUser


#
# Model
#

class Restaurant(AbstractBaseUser):
    """
    """

    # Restaurant's personnal fields (REQUIRED)
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'This email address is already used by another restaurant.',
            'max_length': ''
        },
        help_text=''
    )

    name = models.CharField(
        max_length=32,
        error_messages={
            'max_length': ''
        },
        help_text=''
    )

    phone_number = models.CharField(
        unique=True,
        max_length=16,
        error_messages={
            'unique': 'This phone number is already used by another restaurant.',
            'max_length': ''
        },
        help_text=''
    )

    # Restaurant's location fields (REQUIRED)
    # country

    # city

    # zip_code

    # location

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

    # Restaurant's composition fields (OPTIONNAL)
    

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
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'name', 'phone_number', 'address_part_1']

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
