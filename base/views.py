from django.shortcuts import render, redirect
from .models import Multimedia
from .forms import MultimediaForm


# Create your views here.

def index(req):
    multimedia = Multimedia.objects.all()
    return render(req, 'index.html', {'multimedia': multimedia})


def add_multimedia(req):
    if req.method == 'POST':
        form = MultimediaForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MultimediaForm
    return render(req, 'add_multimedia.html', {'form': form})
