from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project/', blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Message(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()    
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name