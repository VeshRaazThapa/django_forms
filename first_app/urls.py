from django.conf.urls import url
# Create your views here.
from first_app import views
urlpatterns = [
    url(r'^$', views.users, name='users'),
    url(r'^$', views.help, name='help'),
]