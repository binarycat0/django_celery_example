from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from files_app.forms import UploadFileForm
from files_app.models import ObjectWithFile


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ObjectWithFile(file=request.FILES['file'])
            instance.save()
            return JsonResponse('/success/url/')
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})
