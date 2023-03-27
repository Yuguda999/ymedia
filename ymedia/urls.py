from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('edit_photo/<int:pk>/', views.edit_photo, name='edit_photo'),
    path('delete_photo/<int:pk>/', views.delete_photo, name='delete_photo'),
    path('play_music/<int:pk>/', views.play_music, name='play_music'),
    path('play_video/<int:pk>/', views.play_video, name='play_video'),
    path('upload_music/', views.upload_music, name='upload_music'),
    path('edit_music/<int:pk>/', views.edit_music, name='edit_music'),
    path('delete_music/<int:pk>/', views.delete_music, name='delete_music'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('edit_video/<int:pk>/', views.edit_video, name='edit_video'),
    path('delete_video/<int:pk>/', views.delete_video, name='delete_video'),
    path('search/', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
