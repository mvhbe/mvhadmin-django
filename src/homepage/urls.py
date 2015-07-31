from django.conf.urls import include, url
from homepage import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
]
