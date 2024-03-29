# Django imports
from django.shortcuts import get_object_or_404

# Rest_framework imports
from rest_framework import (
    mixins, viewsets, status, response
)

# Serializer imports
from foodie.serializers import (
    FoodieListSerializer, FoodieDetailSerializer,
    FoodieUpdateSerializer, FoodieCreateSerializer
)

# Model imports
from foodie import models, commons

# Other imports
import json


#
# View
#

class FoodieViews(viewsets.ViewSet):
    """
    """
    queryset = models.Foodie.objects.all()

    def list(self, request, format=None):
        serializer = FoodieListSerializer(self.queryset, context=json.dumps('request', request), many=True)
        return response.Response(serializer.data)

        # return response.Response(commons.to_json('message', 'Not implemented yet'), status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, format=None):
        obj = get_object_or_404(self.queryset, pk=pk)

        serializer = FoodieDetailSerializer(obj)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None, format=None):
        obj = get_object_or_404(self.queryset, pk=pk)

        if commons.part_of(request.user, [obj]) is False:
            return response.Response(json.dumps({"message": "Request not permitted"}), status=status.HTTP_403_FORBIDDEN)

        serializer = FoodieUpdateSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(json.dumps({"message": "Foodie updated"}), status=status.HTTP_200_OK)
        return response.Response(json.dumps({"message": "%s" % (serializer.errors)}), status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, format=None):
        serializer = FoodieCreateSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(json.dumps({"message": "Foodie created"}), status=status.HTTP_200_OK)
        return response.Response(json.dumps({"message": "%s" % (serializer.errors)}), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        obj = get_object_or_404(self.queryset, pk=pk)

        if commons.part_of(request.user, [obj]) is False:
            return response.Response(json.dumps({"message": "Request not permitted"}), status=status.HTTP_403_FORBIDDEN)

        obj.is_active = False
        obj.save()
        return response.Response(json.dumps({"message": "Foodie account desactivated"}), status=status.HTTP_200_OK)


class ProfileFoodieViews(viewsets.ViewSet):
    """
    """

    queryset = models.Foodie.objects.all()

    def retrieve(self, request, format=None):
        obj = get_object_or_404(self.queryset, pk=request.user.pk)

        serializer = FoodieDetailSerializer(obj)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, format=None):
        obj = get_object_or_404(self.queryset, pk=request.user.pk)

        serializer = FoodieUpdateSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(json.dumps({"message": "Foodie updated"}), status=status.HTTP_200_OK)
        return response.Response(json.dumps({"message": "%s" % (serializer.errors)}), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        obj = get_object_or_404(self.queryset, pk=request.user.pk)

        obj.is_active = False
        obj.save()
        return response.Response(json.dumps({"message": "Foodie account desactivated"}), status=status.HTTP_200_OK)
