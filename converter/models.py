from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    converted_image = models.ImageField(upload_to='converted/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
