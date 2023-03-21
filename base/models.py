from django.db import models

# Create your models here.

class Multimedia(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title