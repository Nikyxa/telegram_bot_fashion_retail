from django.db import models


class StartDate(models.Model):
    date = models.DateField()


class OwnerName(models.Model):
    name = models.CharField(max_length=255)


class Username(models.Model):
    username = models.EmailField()
