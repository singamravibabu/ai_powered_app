from django.shortcuts import render

# Create your views here.
from .forms import ResumeUploadForm

def home(request):
    return render(request, 'index.html')

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', {'form': ResumeUploadForm()})