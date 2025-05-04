from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet,
)

router = DefaultRouter()
router.register(
    prefix=r"posts",
    viewset=PostViewSet,
    basename="posts",
)
router.register(
    prefix=r"groups",
    viewset=GroupViewSet,
    basename="groups",
)
router.register(
    prefix=r"follow",
    viewset=FollowViewSet,
    basename="follow",
)
router.register(
    prefix=r"posts/(?P<post_id>\d+)/comments",
    viewset=CommentViewSet,
    basename="comments",
)


urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
]
