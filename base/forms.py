from django import forms
from .models import Photo, Music, Video


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['song', 'title', 'artist', 'album']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video', 'title', 'description']
