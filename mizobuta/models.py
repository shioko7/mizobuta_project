from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class Prefecture(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    hazardous_locations_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class DangerousLocation(models.Model):
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    is_dangerous = models.BooleanField(default=False)

    def __str__(self):
        return str(self.prefecture)


@receiver(post_save, sender=DangerousLocation)
def update_hazardous_locations_count(sender, instance, **kwargs):
    prefecture = instance.prefecture
    count = DangerousLocation.objects.filter(prefecture=prefecture, is_dangerous=True).count()
    prefecture.hazardous_locations_count = count
    prefecture.save()

class CustomUser(AbstractUser):
    prefecture = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, null=True)
    birthdate = models.DateField(null=True)

    def __str__(self):
        return self.username
