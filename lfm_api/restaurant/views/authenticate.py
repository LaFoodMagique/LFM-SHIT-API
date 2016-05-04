# Django imports
from django.contrib.auth import (
    login as django_login,
    authenticate as django_auth,
    logout as django_logout
)

# rest_framework imports
from rest_framework import response, status, decorators

# Other imports
import json


#
# Views
#

@decorators.api_view(['POST'])
def restaurant_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode("utf-8"))
            user = django_auth(email=data["email"], password=data["password"])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return response.Response(json.dumps({"message": "You are now connected"}), status=status.HTTP_200_OK)
                else:
                    return response.Response(json.dumps({"message": "The user is not active."}), status=status.HTTP_401_UNAUTHORIZED)
            else:
                return response.Response(json.dumps({"message": "The user doesn\'t exist."}), status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(json.dumps({"message": "%s" % (e)}), status=status.HTTP_400_BAD_REQUEST)
    else:
        return response.Response(json.dumps({"message": "This type of request are not allowed"}), status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(['POST'])
def restaurant_logout(request):
    if request.method == 'POST':
        django_logout(request)
        return response.Response(json.dumps({"message": "You are now logout."}), status=status.HTTP_200_OK)
    else:
        return response.Response(json.dumps({"message": "This type of request are not allowed"}), status=status.HTTP_400_BAD_REQUEST)
