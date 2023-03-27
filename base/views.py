from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Photo, Music, Video
from .forms import PhotoForm, MusicForm, VideoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def home(request):
    photos = Photo.objects.all()
    music = Music.objects.all()
    videos = Video.objects.all()
    return render(request, 'home.html', {'photos': photos, 'music': music, 'videos': videos})


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, 'Your photo has been uploaded.')
            return redirect('home')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})


def upload_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.user = request.user
            music.save()
            messages.success(request, 'Your music has been uploaded.')
            return redirect('home')
    else:
        form = MusicForm()
    return render(request, 'upload_music.html', {'form': form})


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            messages.success(request, 'Your video has been uploaded.')
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})


def edit_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, 'Your photo has been updated.')
            return redirect('home')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'edit_photo.html', {'form': form, 'photo': photo})


def edit_music(request, pk):
    music = get_object_or_404(Music, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES, instance=music)
        if form.is_valid():
            music = form.save(commit=False)
            music.user = request.user
            music.save()
            messages.success(request, 'Your music has been updated.')
            return redirect('home')
    else:
        form = MusicForm(instance=music)
    return render(request, 'edit_music.html', {'form': form, 'music': music})


def edit_video(request, pk):
    video = get_object_or_404(Video, pk=pk, user=request.user)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            messages.success(request, 'Your video has been updated.')
        return redirect('home')
    else:
        form = VideoForm(instance=video)
    return render(request, 'edit_video.html', {'form': form, 'video': video})


def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk, user=request.user)
    photo.delete()
    messages.success(request, 'Your photo has been deleted.')
    return redirect('home')


def delete_music(request, pk):
    music = get_object_or_404(Music, pk=pk, user=request.user)
    music.delete()
    messages.success(request, 'Your music has been deleted.')
    return redirect('home')


def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk, user=request.user)
    video.delete()
    messages.success(request, 'Your video has been deleted.')
    return redirect('home')


def play_music(request, pk):
    music = get_object_or_404(Music, pk=pk, user=request.user)
    return render(request, 'play_music.html', {'music': music})


def play_video(request, pk):
    video = get_object_or_404(Video, pk=pk, user=request.user)
    return render(request, 'play_video.html', {'video': video})


def search(request):
    query = request.GET.get('q')
    photos = Photo.objects.filter(user=request.user, title__icontains=query)
    music = Music.objects.filter(user=request.user, title__icontains=query)
    videos = Video.objects.filter(user=request.user, title__icontains=query)
    return render(request, 'search.html', {'photos': photos, 'music': music, 'videos': videos})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user after registration
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')
