from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name
