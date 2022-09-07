from django.urls import path, include
from rest_framework.routers import DefaultRouter
from basis import views
from rest_framework.authtoken import views as view_token


router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename="post")
router.register(r'comments', views.CommentViewSet, basename="comment")
router.register(r'users', views.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', view_token.obtain_auth_token)
]
