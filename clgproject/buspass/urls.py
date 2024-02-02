from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('routeinfo',views.routeinfo,name='routeinfo'),
    path('payment',views.payment,name='payment'),
    path('contactus',views.contactus,name='contactus')

]