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
            user = Foodie.objects.get(email=email)
            if user.check_password(password):
                return user
        except Exception:
            return None

    def get_user(self, user_id):
        try:
            user = Foodie.objects.get(pk=user_id)
            if user.is_active:
                return user
        except Exception:
            return None
