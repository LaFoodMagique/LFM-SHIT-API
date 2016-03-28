# Restframework imports
from rest_framework import serializers

# Model imports
from restaurant.models import Restaurant


#
# List
#

class RestaurantListSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    url = serializers.HyperlinkedIdentityField(view_name='restaurant:detail')

    class Meta:
        model = Restaurant
        fields = (
            'id', 'url', 'email', 'name', 'phone_number'
        )

#
# Detail
#

class RestaurantDetailSerializer(serializers.HyperlinkedModelSerializer):
    """
    """

    class Meta:
        model = Restaurant
        fields = (
            'id', 'email', 'name', 'phone_number',
            'address_part_1', 'address_part_2',
            'registration_date'
        )


#
# Update
#

class RestaurantUpdateSerializer(serializers.HyperlinkedModelSerializer):
    """
    """

    class Meta:
        model = Restaurant
        fields = (
            'email', 'password', 'name', 'phone_number',
            'address_part_1', 'address_part_2',
        )

    def update(self, instance, data):
        for field, value in data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance


#
# Create
#

class RestaurantCreateSerializer(serializers.HyperlinkedModelSerializer):
    """
    """

    class Meta:
        model = Restaurant
        fields = (
            'email', 'password', 'name', 'phone_number',
            'address_part_1', 'address_part_2',
        )

    def create(self, data):
        password = data.pop('password', None)
        instance = self.Meta.model(**data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


#
# Delete
#
