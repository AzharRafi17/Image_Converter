from django.urls import path
from .views import upload_image, progress

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('progress/<int:image_id>/', progress, name='progress'),
]
