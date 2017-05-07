from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
# from rest_framework_jwt.views import obtain_jwt_token

from auth_api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Todo API', description='RESTful API for Todo')),

    url(r'^$', views.api_root),
    # url(r'^', include('auth.urls', namespace='auth')),
    url(r'^', include('users.urls', namespace='users')),
    url(r'^', include('todos.urls', namespace='todos')),
]
