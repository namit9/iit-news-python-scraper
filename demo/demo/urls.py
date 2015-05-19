from django.conf.urls import include, url

import views
urlpatterns = [
    url(r'^news/$', views.index, name='index'),
    url(r'^api/$', views.api, name='api'),
]
