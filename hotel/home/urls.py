from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<city_id>[0-9]+)/$',views.city,name='city'),
    url(r'^(?P<city_id>[0-9]+)/book$',views.book,name='book'),
    url(r'^(?P<city_id>[0-9]+)/book/user_details$',views.user_details,name='user_details'),
    url(r'^1/book/user_details/confirmation$',views.confirmation,name='confirmation')
]
