from django.urls import path
from .views import upload_image, get_random_image

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('random/', get_random_image, name='get_random_image'),
]
