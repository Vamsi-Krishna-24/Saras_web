from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='Home'), 
    path('home/', views.Home, name='Home_login'),  
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]

