from django.conf.urls import include, url
from kalenders import views

urlpatterns = [
    url(r'^$', views.kalenders, name='kalenders'),
]
