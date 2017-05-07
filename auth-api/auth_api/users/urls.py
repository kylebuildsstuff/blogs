from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views


urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]
