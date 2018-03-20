from django.conf.urls import url

from gcn import views

urlpatterns = [
    # Url links for other core pages
    url(r'^$', views.home, name='home'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^club_list/$', views.club_list, name='club_list'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^reviews/$', views.reviews, name='reviews'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add_night/$', views.add_night, name='add_night'),

    # Url links for club webpages

    url(r'^bamboo/$', views.bamboo, name='bamboo'),
    url(r'^cathouse/$', views.cathouse, name='cathouse'),
    url(r'^firewater/$', views.firewater, name='firewater'),
    url(r'^garage/$', views.garage, name='garage'),
    url(r'^hive/$', views.hive, name='hive'),
    url(r'^kokomo/$', views.kokomo, name='kokomo'),
    url(r'^kushion/$', views.kushion, name='kushion'),
    url(r'^la_cheetah/$', views.la_cheetah, name='la_cheetah'),
    url(r'^mango/$', views.mango, name='mango'),
    url(r'^polo/$', views.polo, name='polo'),
    url(r'^sanctuary/$', views.sanctuary, name='sanctuary'),
    url(r'^shimmy/$', views.shimmy, name='shimmy'),
    url(r'^subclub/$', views.subclub, name='subclub'),
    url(r'^swg3/$', views.swg3, name='swg3'),
    url(r'^viper/$', views.viper, name='viper'),

]
