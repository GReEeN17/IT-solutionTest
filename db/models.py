from django.db import models

class Requests(models.Model):
    request = models.CharField(max_length=50)
