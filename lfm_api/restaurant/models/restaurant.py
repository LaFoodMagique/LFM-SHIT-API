# Django imports
from django.db import models
from django.utils import timezone

# Model imports
from base_user.models import BaseUser


#
# Model
#

class Restaurant(BaseUser):
    """
    """

    #
    # Restaurant's personnal fields (REQUIRED)
    #
    # Go to the base_user.py file,
    # in this file you will find the BaseUser class where the others informations are modelised.
    #
    name = models.CharField(
        max_length=32,
        error_messages={
            'max_length': ''
        },
        help_text=''
    )

    #
    # Restaurant's location fields (REQUIRED)
    #
    # Go to the base_user.py file,
    # in this file you will find the BaseUser class where this informations are modelised.
    #


    # Restaurant's composition fields (OPTIONNAL)
    

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
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    REQUIRED_FIELDS = ['name']

    # Class properties

    # Class functions
