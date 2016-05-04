# Django imports
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import (
    login as django_login,
    authenticate as django_auth,
    logout as django_logout
)

# rest_framework imports
from rest_framework import response, status, decorators

# Model imports
from foodie import commons

#
# Views
#

@decorators.api_view(['POST'])
def foodie_login(request):
    if request.method == 'POST':
        try:
            user = django_auth(email=request.POST.get('email'), password=request.POST.get('password'))
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return response.Response(commons.to_json('message', 'You are now connected'), status=status.HTTP_200_OK)
                else:
                    return response.Response(commons.to_json('message', 'The user is not active.'), status=status.HTTP_401_UNAUTHORIZED)
            else:
                return response.Response(commons.to_json('message', 'The user doesn\'t exist.'), status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(commons.to_json('message', '%s' % (e)), status=status.HTTP_400_BAD_REQUEST)
    else:
        return response.Response(commons.to_json('message', 'This type of request are not allowed'), status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(['POST'])
def foodie_logout(request):
    if request.method == 'POST':
        django_logout(request)
        return response.Response(commons.to_json('message', 'You are now logout.'), status=status.HTTP_200_OK)
    else:
        return response.Response(commons.to_json('message', 'This type of request are not allowed'), status=status.HTTP_400_BAD_REQUEST)