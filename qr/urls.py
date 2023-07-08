from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('sertificate-form', sertificate_form, name='sertificate-form'),
    path('sertificate-list', sertificate_list, name='sertificate-list'),
    path('sertificate-detail/<str:pk>/', sertificate_detail, name='sertificate-detail'),
    path('settings/', settings, name='settings'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]