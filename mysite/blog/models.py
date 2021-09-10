from django.db import models

# Create your models here.
class Post(models.Model):
    description = models.CharField(max_length=1200)
    image = models.ImageField(null=True, upload_to = 'images')
    title = models.CharField(max_length=200)
    date_pub = models.DateField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __str__(self):
        return self.title




