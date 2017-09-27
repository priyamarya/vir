from django.conf.urls import url
from .views import login, register, logout, user_details_entry1, user, profile_edit


urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^register/$', register, name="signup"),
    url(r'^logout/$', logout, name="logout"),
    #url(r'^userdetailsentry/$', user_details_entry1, name="details"),
    url(r'^user/(?P<username>\w+)/$', user, name="user"),
    url(r'^userdetailsentry/(?P<username>\w+)/$', profile_edit, name="profile_edit"),



]
