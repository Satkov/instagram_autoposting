from django.urls import path
from .views import APIPhotoPost, APIVideoPost

urlpatterns = [
    path('api/v1/photoposts/<int:user_id>', APIPhotoPost.as_view()),
    path('api/v1/photoposts/<int:user_id>/<str:caption>/<str:img_url>/'
         '<int:location_id>/<str:user_tags>/<str:token>/<int:date_pub>',
         APIPhotoPost.as_view()),
    path('api/v1/photoposts/<int:id>/<str:new_field>/<str:value>', APIPhotoPost.as_view()),
    path('api/v1/photoposts_delete/<int:id>', APIPhotoPost.as_view()),
    path('api/v1/videoposts/<int:user_id>', APIVideoPost.as_view()),
    path('api/v1/videoposts/<int:user_id>/<str:caption>/<str:vid_url>/'
         '<int:location_id>/<int:thump_offset>/<str:token>/<int:date_pub>',
         APIVideoPost.as_view()),
    path('api/v1/videoposts/<int:id>/<str:new_field>/<str:value>', APIVideoPost.as_view()),
    path('api/v1/videoposts_delete/<int:id>', APIVideoPost.as_view()),
]
