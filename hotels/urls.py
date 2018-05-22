from django.urls import path

from . import views

urlpatterns = [	
    path('', views.get_city, name='get_city'),
    path('get_cities/', views.get_cities, name='get_cities'),    
]
