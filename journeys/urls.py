"""List of urls for application Journeys"""
from django.urls import re_path

from .views import JourneyCreate, JourneyUpdate, JourneyDelete, JourneyList

urlpatterns = [
    re_path(r'^$', JourneyList.as_view(), name='journey_index'),
    re_path(r'^add/$', JourneyCreate.as_view(), name='journey_add'),
    re_path(r'^(?P<pk>[0-9]+)/update/$', JourneyUpdate.as_view(), name='journey_update'),
    re_path(r'^(?P<pk>[0-9]+)/detail/$', JourneyUpdate.as_view(), name='journey_detail'),
    re_path(r'^(?P<pk>[0-9]+)/delete/$', JourneyDelete.as_view(), name='journey_delete'),
    re_path(r'^statistics/$', JourneyCreate.as_view(), name='journey_add'),
    
]
