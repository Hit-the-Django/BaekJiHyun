from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from posts.views import *
from posts.views import class_view

# router=routers.DefaultRouter()
# router.register('posts', PostModelViewSet)
# router.register('comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Function Based View
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/', function_view),
    # Class Based View
    path('cbv/', class_view.as_view()), # as_view: 진입 메소드

    # path('', index, name='index'),
    # path('', include(router.urls)),
    # path('posts/', include('posts.urls', namespace='posts')), #앱.url로 전달
    path('accounts/', include('accounts.urls', namespace='accounts')),

    path('posts/',PostListCreateView.as_view(), name='post-list-create'),
    path('posts/',PostListRetrieveUpdateView.as_view(), name='post-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)