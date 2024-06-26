from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet

v1_router = DefaultRouter()

v1_router.register(
    r'v1/posts',
    PostViewSet,
)

urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]
