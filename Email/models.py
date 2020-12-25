from django.db import models

# Create your models here.

class EmailModel(models.Model):
    Email = models.EmailField(default='')
    Message = models.TextField()
