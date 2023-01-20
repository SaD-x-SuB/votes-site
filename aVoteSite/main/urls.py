from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'main'),
    path('accounts/login',views.index,name='Acc'),
    path('accounts/profile',views.prof,name='profile'),
]
