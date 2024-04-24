# Ansar Khan

from django.db import models
from django.core.validators import FileExtensionValidator
class UploadedImage(models.Model):
    image = models.ImageField(
        upload_to='images/', 
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'], message='Unknown File.')]
    )