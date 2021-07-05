from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup.as_view(), name='signup'),
    path('main/',views.getInfo.as_view(), name='main'),
    path('thankyou/', views.test, name='test')
]


