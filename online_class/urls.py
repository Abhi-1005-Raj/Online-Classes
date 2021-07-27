from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index , name='Online classes Sign-In'),
    
    path('home/', views.home , name='Online classes home'),
    
    path('about/', views.about , name='Online classes about'),
]