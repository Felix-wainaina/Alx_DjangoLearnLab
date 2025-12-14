from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # The order matters; static paths should usually come before router includes
    path('feed/', FeedView.as_view(), name='post_feed'),
    path('', include(router.urls)),
]