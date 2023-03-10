from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    photo = models.ImageField()
    

# Create your models here.
class FilesUpload(models.Model):
    userid = models.IntegerField()
    file = models.FileField()
    
