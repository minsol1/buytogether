from django.db import models

# Create your models here.

class Pur(models.Model):
    CATEGORY_CHOICES = [(0,'식재료'),(1,'생필품'),(2,'OTT'),(3,'배달')]
    title = models.CharField(max_length=200)
    body = models.TextField()
    writeDate = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    category = models.IntegerField(choices=CATEGORY_CHOICES,
                                 blank=False,
                                 null=False,
                                 default=0)
    wpeople = models.IntegerField()
    peopole = models.IntegerField()
    price = models.IntegerField()
    location=models.CharField(max_length=300)
    lat = models.FloatField() #위도
    long = models.FloatField() #경도
    good = models.IntegerField()
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.title
    