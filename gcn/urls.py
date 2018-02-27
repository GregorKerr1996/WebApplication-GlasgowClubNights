from django.conf.urls import url
from gcn import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]