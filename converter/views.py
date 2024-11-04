from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageUpload
from .tasks import convert_to_png

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            convert_to_png.delay(image.id)
            return redirect('progress', image_id=image.id)
    else:
        form = ImageUploadForm()
    return render(request, 'converter/upload.html', {'form': form})

def progress(request, image_id):
    image = ImageUpload.objects.get(id=image_id)
    return render(request, 'converter/progress.html', {'image': image})
