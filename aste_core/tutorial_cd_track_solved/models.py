from django.db import models


class CD(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField(null=True)


class Track(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    cd = models.ForeignKey(CD, related_name="tracks")
