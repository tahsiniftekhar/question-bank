from django.db import models

class User(models.Model):
    username = models.CharField(max_length=250, unique=True)
    full_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    def __str__(self):
        return self.username