from django.conf.urls import url
from .views import all_cards, view_card, new_card, search,edit_card


urlpatterns = [
    url(r'^all/$', all_cards, name="all"),
    url(r'^newcard/$', new_card),
    url(r'^all/(?P<card_id>\d+)/$', view_card),
    # url(r'^likes/(?P<card_id>\d+)/$', likes, name="like"),
    url(r'^found/', search),
    url(r'^edit/(?P<card_id>\d+)/$',edit_card, name="edit")
    
]
