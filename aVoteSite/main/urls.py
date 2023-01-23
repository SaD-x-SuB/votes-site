from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'main'),
    path('accounts/login',views.index,name='Acc'),
    path('accounts/profile',views.prof,name='profile'),
    path('accounts/profile/myVotes', views.myVotes, name='myVotes'),
    path('accounts/profile/myVotes/create', views.create, name='createVote'),
    path("accounts/profile/myVotes/ref", views.refactor, name = "refact"),
]
