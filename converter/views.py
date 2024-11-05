from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageUpload
from .tasks import convert_to_png
from django.contrib import messages

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            
            image = request.FILES['image']
            if image.content_type in ['image/jpeg', 'image/jpg']:
                image_instance = form.save()  # Save the form and get the instance
                convert_to_png.delay(image_instance.id)
                return redirect('progress', image_id=image_instance.id)  # Use the instance's ID
            else:
                messages.error(request, 'Please upload a JPG or JPEG image.')
                return render(request, 'converter/upload.html', {'form': form})
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = ImageUploadForm()
    return render(request, 'converter/upload.html', {'form': form})

def progress(request, image_id):
    image = ImageUpload.objects.get(id=image_id)
    return render(request, 'converter/progress.html', {'image': image})



# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.save()
#             convert_to_png.delay(image.id)
#             return redirect('progress', image_id=image.id)
#     else:
#         form = ImageUploadForm()
#     return render(request, 'converter/upload.html', {'form': form})