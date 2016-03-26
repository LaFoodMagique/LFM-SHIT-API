# Django imports
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import (
    mixins, viewsets, status, response
)

# Serializer imports
from foodie.serializers.foodie import (
    FoodieListSerializer, FoodieDetailSerializer,
    FoodieUpdateSerializer, FoodieCreateSerializer
)

# Model imports
#from foodie.models.foodie import Foodie
from foodie import models, commons


#
# View
#

class FoodieViews(viewsets.ViewSet):
    """
    """
    queryset = models.foodie.Foodie.objects.all()

    def list(self, request, format=None):
        foodie = get_object_or_404(self.queryset, pk=request.user.pk)
        serializer = FoodieListSerializer(foodie, context=commons.to_json('request', request))
        return response.Response(serializer.data)

        return response.Response(commons.to_json('message', 'Not implemented yet'), status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, format=None):
        foodie = get_object_or_404(self.queryset, pk=pk)

        serializer = FoodieDetailSerializer(foodie)
        return response.Response(serializer.data)

    def update(self, request, pk=None, format=None):
        foodie = get_object_or_404(self.queryset, pk=pk)

        if part_of(request.user, [foodie]) is False:
            return response.Response(commons.to_json('message', 'Request not permitted'), status=status.HTTP_403_FORBIDDEN)

        serializer = FoodieUpdateSerializer(foodie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(commons.to_json('message', 'Foodie updated'), status=status.HTTP_200_OK)
        return response.Response(commons.to_json('message', 'Missing or bad parameters'), status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, format=None):
        serializer = FoodieCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(commons.to_json('message', 'Foodie created'), status=status.HTTP_200_OK)
        return response.Response(commons.to_json('message', 'Missing or bad parameters'), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        foodie = get_object_or_404(self.queryset, pk=pk)

        if part_of(request.user, [foodie]) is False:
            return response.Response(commons.to_json('message', 'Request not permitted'), status=status.HTTP_403_FORBIDDEN)

        foodie.is_active = False
        foodie.save()
        return response.Response(commons.to_json('message', 'Foodie desactivated'), status=status.HTTP_200_OK)
