# Model imports
from restaurant.models import Restaurant


#
# Back-End
#

class RestaurantBackEnd(object):
    """
    """

    def authenticate(self, email=None, password=None):
        try:
            user = Restaurant.objects.get(email=email)
            if user.check_password(password):
                return user
        except Restaurant.DoestNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = Restaurant.objects.get(pk=user_id)
            if user.is_active:
                return user
        except Restaurant.DoestNotExist:
            return None
