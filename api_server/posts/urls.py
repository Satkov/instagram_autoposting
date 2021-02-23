from django.urls import path
from .views import APIPhotoPost, APIVideoPost

urlpatterns = [
    path('api/v1/photoposts/', APIPhotoPost.as_view()),
    path('api/v1/videoposts/', APIVideoPost.as_view()),
]
