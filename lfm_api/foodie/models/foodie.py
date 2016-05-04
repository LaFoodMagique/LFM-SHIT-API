# Django imports
from django.db import models
from django.utils import timezone

# Model imports
from base_user.models import BaseUser


#
# Models
#

GENDER_TYPES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class Foodie(BaseUser):
    """
    """

    #
    # User's personnal fields (REQUIRED)
    #
    # Go to the base_user.py file,
    # in this file you will find the BaseUser class where the others informations are modelised.
    #
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

    #
    # User's location fields (REQUIRED)
    #
    # Go to the base_user.py file,
    # in this file you will find the BaseUser class where this informations are modelised.
    #

    #
    # User's personnal fields (OPTIONNAL)
    #
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

    #
    # Account's fields
    #
    # Go to the base_user.py file,
    # in this file you will find the BaseUser class where this informations are modelised.
    #

    #
    # Class settings
    #
    # Go to the base_user.py file,
    # in this file you will find the BaseUser class where the others informations are modelised.
    #
    class Meta:
        verbose_name = 'foodie'
        verbose_name_plural = 'foodies'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    #
    # Class properties
    #
    # Go to the base_user.py file,
    # in this file you will find the BaseUser class where the others informations are modelised.
    #

    #
    # Class functions
    #
    # Go to the base_user.py file,
    # in this file you will find the BaseUser class where the others informations are modelised.
    #
    def get_username(self):
        if not self.username:
            return self.get_full_name()
        return self.username

    def get_short_name(self):
        return self.last_name

    def get_full_name(self):
        return "%s %s" % (self.last_name, self.first_name)
