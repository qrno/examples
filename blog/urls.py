from django.urls import path
from .views import index, number, posts

urlpatterns = [
    path('', index),
    path('user/<int:num>', number),
    path('posts', posts)
]
