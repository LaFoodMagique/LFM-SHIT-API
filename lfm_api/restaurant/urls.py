# Django imports
from django.conf.urls import url

# View imports
from .views import (
    RestaurantViews, ProfileRestaurantViews,
    restaurant_login, restaurant_logout
)


#
# URLS
#

urlpatterns = [
    url(r'^auth/login/$', restaurant_login, name='login'),
    url(r'^auth/logout/$', restaurant_logout, name='logout'),
    url(r'^auth/register/$', RestaurantViews.as_view({'post': 'create'}), name='register'),

    url(r'^profile/$', ProfileRestaurantViews.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'}), name='profile'),

    url(r'^$', RestaurantViews.as_view({'get': 'list'}), name='restaurants'),
    url(r'^(?P<pk>[0-9]+)/$', RestaurantViews.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'}), name='restaurant'),
]
