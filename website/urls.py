from django.conf.urls import url
import website.views as views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]