#
from django.db import models
from django.utils import timezone

#
from foodie.commons import MARKS


#
#   Model
#

class RestaurantComment(models.Model):
    """
    """

    foodie = models.ForeignKey(
        'foodie.Foodie',
        related_name='restaurant_comments',
        help_text=''
    )

    restaurant = models.ForeignKey(
        'restaurant.Restaurant',
        related_name='user_comments',
        help_text=''
    )

    comment = models.TextField(
        blank=True,
        null=True,
        help_text=''
    )

    mark = models.IntegerField(
        choices=MARKS,
        help_text=''
    )

    creation_date = models.DateTimeField(
        default=timezone.now,
        help_text=''
    )
