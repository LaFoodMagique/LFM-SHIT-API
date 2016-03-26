# Restframework imports
from rest_framework import serializers

# Model imports
from foodie.models.foodie import Foodie


#
# List
#

class FoodieListSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    url = serializers.HyperlinkedIdentityField(view_name='foodie:info')
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = Foodie
        fields = (
            'id', 'url', 'email', 'full_name', 'phone_number'
        )


#
# Detail
#

class FoodieDetailSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    username = serializers.CharField(source='get_username', read_only=True)

    class Meta:
        model = Foodie
        fields = (
            'id', 'email', 'first_name', 'last_name', 'full_name', 'phone_number',
            'address_part_1', 'address_part_2',
            'username', 'birth_date', 'gender', 'registration_date'
        )


#
# Update
#

class FoodieUpdateSerializer():
    """
    """

    class Meta:
        model = Foodie
        fields = (
            'email', 'password', 'first_name', 'last_name', 'phone_number',
            'address_part_1', 'address_part_2',
            'username', 'birth_date', 'gender'
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

class FoodieCreateSerializer(serializers.HyperlinkedModelSerializer):
    """
    """


    class Meta:
        model = Foodie
        fields = (
            'email', 'password', 'first_name', 'last_name', 'phone_number',
            'address_part_1', 'address_part_2',
            'username', 'birth_date', 'gender'
        )

    def create(self, instance, data):
        for field, value in data.item():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance

#
# Delete
#
