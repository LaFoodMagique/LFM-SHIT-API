# Model imports
from foodie.models import Foodie


#
# Back-End
#

class FoodieBackEnd(object):
    """
    """

    def authenticate(self, email=None, password=None):
        try:
            user = Foodie.object.get(email=email)
            if user.check_password(password):
                return user
        except Foodie.DoestNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = Foodie.object.get(pk=user_id)
            if user.is_active:
                return user
        except Foodie.DoestNotExist:
            return None
