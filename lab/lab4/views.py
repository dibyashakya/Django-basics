# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FileUpload
from .models import UploadedFile


def upload_file(request):
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)

        if form.is_valid():
            # Save file to database
            uploaded_file = UploadedFile(
                file=form.cleaned_data['file']
            )
            uploaded_file.save()

            messages.success(request, 'File uploaded successfully!')
            return redirect('upload_success')
    else:
        form = FileUpload()

    return render(request, 'lab4/upload.html', {'form': form})


def upload_success(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'lab4/success.html', {'files': files})