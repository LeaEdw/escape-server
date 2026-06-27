from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from escapeapi.views import (
    login_user,
    register_user,
    UserViewSet,
    LocationViewSet,
    GameViewSet,
    UserRatingViewSet,
    EscapeTimeViewSet,
    CommentViewSet,
    ReactionViewSet,
    UserReactionViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, basename='user')
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'games', GameViewSet, basename='game')
router.register(r'ratings', UserRatingViewSet, basename='rating')
router.register(r'escapetimes', EscapeTimeViewSet, basename='escapetime')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'reactions', ReactionViewSet, basename='reaction')
router.register(r'userreaction', UserReactionViewSet, basename='userreaction')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user)
]

