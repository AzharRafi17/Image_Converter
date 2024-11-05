from django import forms
from .models import ImageUpload
from django.core.exceptions import ValidationError

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']

def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.lower().endswith(('.jpg', '.jpeg')):
                raise ValidationError('Please upload a file in JPG or JPEG format.')
        return image    