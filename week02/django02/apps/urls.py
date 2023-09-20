from django.urls import path
from apps.views import *

urlpatterns = [
    path('hungry/', index),
    path('sleep/', intro),
    path('', market),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new', post_new, name='post_new'),

]