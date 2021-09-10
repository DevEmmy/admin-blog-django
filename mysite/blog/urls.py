from django.contrib import admin
from django.urls import path, include
from .views import homepage, details


urlpatterns = [
    path('', homepage, name='homepage'),
    path('details/<int:post_id>', details, name='details')
    
]
