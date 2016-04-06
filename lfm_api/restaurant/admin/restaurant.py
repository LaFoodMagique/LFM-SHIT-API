# Django imports
from django.contrib import admin

# Model imports
from restaurant.models import Restaurant


#
# Admin models
#

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """
    """

    fieldsets = [
        ('Personnal fields', {
                'fields': [
                    ('email', 'password'), 'name', 'phone_number'
                ]
            }
        ),
        ('Location fields', {
                'fields': [
                    ('address_part_1', 'address_part_2'),
                ]
            }
        ),
    ]


