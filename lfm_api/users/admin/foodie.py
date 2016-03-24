# Django imports
from django.contrib import admin

# Model imports
from users.models import Foodie


#
# Admin models
#

@admin.register(Foodie)
class FoodieAdmin(admin.ModelAdmin):
    """
    """

    fieldsets = [
        ('Personnal fields', {
                'fields': [
                    ('email', 'password'), ('first_name', 'last_name'), 'phone_number'
                ]
            }
        ),
        ('Location fields', {
                'fields': [
                    ('address_part_1', 'address_part_2')
                ]
            }
        ),
        ('Personnal optionnal fields', {
                'fields': [
                    'username', 'birth_date', 'gender'
                ]
            }
        )
    ]

    list_display = ['email', 'get_full_name', 'phone_number']
    list_search = ['email', 'phone_number', 'last_name']
