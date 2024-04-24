from django.urls import path
from .views import CustomImageView, PictureUploadView

urlpatterns = [
    path('perform-analysis/', CustomImageView.as_view(), name='perform_analysis'),
    path('upload-picture/', PictureUploadView.as_view(), name='upload_picture'),
]
