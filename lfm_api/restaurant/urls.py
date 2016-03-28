# Django imports
from django.conf.urls import url

# View imports
from .views import RestaurantViews


#
# URLS
#

urlpatterns = [
    # url(r'^auth/login/$'),
    # url(r'^auth/logout/$'),
    url(r'^auth/register/$', RestaurantViews.as_view({'post': 'create'}), name='register'),

    #url(r'^profile/$'),

    url(r'^$', RestaurantViews.as_view({'get': 'list'}), name='restaurants'),
    url(r'^(?P<pk>[0-9]+)/$', RestaurantViews.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'}), name='detail'),
]
