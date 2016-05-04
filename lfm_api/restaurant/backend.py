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
            if user.check_password(password) and user.type is "Restaurant":
                return user
        except Exception:
            return None

    def get_user(self, user_id):
        try:
            user = Restaurant.objects.get(pk=user_id)
            if user.is_active:
                return user
        except Exception:
            return None
