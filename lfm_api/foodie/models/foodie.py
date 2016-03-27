# Django imports
from django.db import models
from django.utils import timezone

# Model imports
from django.contrib.auth.models import AbstractBaseUser


#
# Models
#

GENDER_TYPES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class Foodie(AbstractBaseUser):
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

    first_name = models.CharField(
        max_length=32,
        error_messages={
            'max_length': ''
        },
        help_text=''
    )

    last_name = models.CharField(
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

    # User's personnal fields (OPTIONNAL)
    username = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        error_messages={
            'max_length': ''
        },
        help_text=''
    )

    birth_date = models.DateField(
        blank=True,
        null=True,
        help_text=''
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_TYPES,
        blank=True,
        null=True,
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
        verbose_name = 'foodie'
        verbose_name_plural = 'foodies'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name', 'phone_number', 'address_part_1']

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
    def get_username(self):
        if not self.username:
            return self.get_full_name()
        return self.username

    def get_short_name(self):
        return self.last_name

    def get_full_name(self):
        return "%s %s" % (self.last_name, self.first_name)
