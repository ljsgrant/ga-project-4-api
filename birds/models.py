from django.db import models


class Bird(models.Model):
    # bird_sighted = models.ForeignKey("birds.Bird", related_name="sightings", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.owner}"