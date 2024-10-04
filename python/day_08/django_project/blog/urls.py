from django.urls import path
from .views import post_list, new_post 
from .views import post_detail

urlpatterns = [
    path('', post_list, name='post_list'),
    path('new_post/', new_post, name='new_post'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]

