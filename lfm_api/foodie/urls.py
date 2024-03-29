# Django imports
from django.conf.urls import url

# View imports
from .views import (
    FoodieViews, ProfileFoodieViews,
    foodie_login, foodie_logout
)


#
# URLS
#

urlpatterns = [
    url(r'^auth/login/$', foodie_login, name='login'),
    url(r'^auth/logout/$', foodie_logout, name='logout'),
    url(r'^auth/register/$', FoodieViews.as_view({'post': 'create'}), name='register'),

    url(r'^profile/$', ProfileFoodieViews.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'}), name='profile'),

    url(r'^$', FoodieViews.as_view({'get': 'list'}), name='foodies'),
    url(r'^(?P<pk>[0-9]+)/$', FoodieViews.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'}), name='detail'),
]
