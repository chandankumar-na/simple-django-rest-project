from django.db import models

class Users(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
        