from django.db import models

# Create your models here.

class Task(models.Model):
    amount = models.IntegerField()
    bank = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.amount)

