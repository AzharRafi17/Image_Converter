from celery import shared_task
from .models import ImageUpload
from PIL import Image
import os

@shared_task(bind=True)
def convert_to_png(self, image_id):
    image_instance = ImageUpload.objects.get(id=image_id)
    image_instance.status = 'Processing'
    image_instance.save()

    img_path = image_instance.image.path
    img = Image.open(img_path)
    output_path = os.path.splitext(img_path)[0] + '.png'
    img.save(output_path, 'PNG')

    image_instance.converted_image.name = output_path.replace('media/', '')
    image_instance.status = 'Completed'
    image_instance.save()
    return True
