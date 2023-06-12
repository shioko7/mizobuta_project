# models.py

from django.db import models

class Prefecture(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class HazardousLocation(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class DangerousLocation(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_dangerous = models.BooleanField(default=False)

    def __str__(self):
        return str(self.city)
