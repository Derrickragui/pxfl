from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('confirmlogin/', views.otphandler, name='confirmlogin'),
    path('redirectuser/', views.redirectuser, name='redirectuser')
]
