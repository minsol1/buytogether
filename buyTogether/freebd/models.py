from django.db import models

# Create your models here.
class Free(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    writeDate = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True,null=True,upload_to='free_photo')
    # good = models.IntegerField()
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    body = models.TextField()
    writeDate = models.DateTimeField(auto_now_add=True)
    freeId = models.ForeignKey(Free, on_delete=models.CASCADE)
