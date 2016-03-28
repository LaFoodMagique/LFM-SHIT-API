# Django imports
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import (
    mixins, viewsets, status, response
)

# Serializer imports
from restaurant.serializers import (
    RestaurantListSerializer, RestaurantDetailSerializer,
    RestaurantUpdateSerializer, RestaurantCreateSerializer
)

# Model imports
from restaurant import models
from foodie import commons


#
# Views
#

class RestaurantViews(viewsets.ViewSet):
    """
    """

    queryset = models.Restaurant.objects.all()

    def list(self, request, format=None):
        serializer = RestaurantListSerializer(self.queryset, context=commons.to_json('request', request), many=True)
        return response.Response(serializer.data)

        # return response.Response(commons.to_json('message', 'Not implemented yet'), status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, format=None):
        obj = get_object_or_404(self.queryset, pk=pk)

        serializer = RestaurantDetailSerializer(obj)
        return response.Response(serializer.data)

    def update(self, request, pk=None, format=None):
        obj = get_object_or_404(self.queryset, pk=pk)

        if commons.part_of(request.user, [obj]) is False:
            return response.Response(commons.to_json('message', 'Request not permitted'), status=status.HTTP_403_FORBIDDEN)

        serializer = RestaurantUpdateSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(commons.to_json('message', 'Restaurant updated'), status=status.HTTP_200_OK)
        return response.Response(commons.to_json('message', 'Missing or bad parameters'), status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, format=None):
        serializer = RestaurantCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(commons.to_json('message', 'Restaurant created'), status=status.HTTP_200_OK)
        return response.Response(commons.to_json('message', 'Missing or bad parameters'), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        obj = get_object_or_404(self.queryset, pk=pk)

        if commons.part_of(request.user, [obj]) is False:
            return response.Response(commons.to_json('message', 'Request not permitted'), status=status.HTTP_403_FORBIDDEN)

        obj.is_active = False
        obj.save()
        return response.Response(commons.to_json('message', 'Restaurant desactivated'), status=status.HTTP_200_OK)
