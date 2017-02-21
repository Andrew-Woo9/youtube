from django.conf.urls import url

from video import views

app_name = 'video'
urlpatterns = [
    url(r'^$', views.search_view, name='search'),
]
