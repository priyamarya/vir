from django.conf.urls import url
from .views import likes

urlpatterns = [
    url(r'^like/(?P<card_id>\d+)/$', likes, name='like'),
]
