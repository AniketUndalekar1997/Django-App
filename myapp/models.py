from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)



class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

