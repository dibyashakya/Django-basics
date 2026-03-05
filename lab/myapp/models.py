from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True),
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.username