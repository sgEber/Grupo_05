from django.urls import path
from . import views

urlpatterns = [
    path('', views.homes, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'), 
    
]

