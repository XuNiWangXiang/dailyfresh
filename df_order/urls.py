from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.order),
    url(r'^order_handls/$',views.order_handls),
    url(r'^test/$',views.test),

]