# Django imports
from django.conf.urls import url

# View imports
from .views import FoodieViews


#
# URLS
#

urlpatterns = [
    # url(r'^auth/login/$'),
    # url(r'^auth/logout/$'),
    url(r'^auth/register/$', FoodieViews.as_view({'post': 'create'}), name='register'),

    #url(r'^profile/$'),

    url(r'^$', FoodieViews.as_view({'get': 'list'}), name='foodies'),
    url(r'^(?P<pk>[0-9]+)/$', FoodieViews.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'}), name='info'),
]
