from django.db import models

# Create your models here.
class Chef(models.Model):
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    year_of_birth = models.DateField(null=True, default=None, blank=True)
    bio = models.TextField(default=None)

    def __str__(self):
        return self.last_name

class Dishes(models.Model):
    name = models.CharField(max_length=100)
    time = models.IntegerField(null=True, default=None)
    ingredients = models.TextField()
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=500)
    openhour = models.IntegerField(null=True, default=None)
    dishes = models.ManyToManyField(Dishes)

    def __str__(self):
        return self.name



