from django.contrib import admin
from django.urls import path

from .views import *

app_name='posts'

urlpatterns = [
    path('', post_list_view, name= 'post-list'),
    path('new/', post_create_view),
    path('<int:id>/', post_detail_view),
    path('<int:id>/edit', post_update_view),
    path('<int:id>/delete', post_delete_view),
]