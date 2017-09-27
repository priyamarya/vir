from django.conf.urls import url
from .views import write_comment

urlpatterns = [
	url(r'^comment/(?P<card_id>\d+)/$', write_comment, name='comment'),

]