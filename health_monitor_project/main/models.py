from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BloodPressureReading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    heart_rate = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.systolic}/{self.diastolic} ({self.created_at})"