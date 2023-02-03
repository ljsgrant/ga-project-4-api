from django.db import models


class Sighting(models.Model):
    bird_sighted = models.ForeignKey(
        "birds.Bird", related_name="sightings", on_delete=models.CASCADE)
    sighted_at_datetime = models.DateTimeField()
    location_lat = models.FloatField(max_length=10)
    location_long = models.FloatField(max_length=10)
    notes = models.CharField(max_length=500)
    owner = models.ForeignKey(
        "jwt_auth.User", related_name="sightings", on_delete=models.CASCADE)
    image = models.CharField(max_length=40, blank=True)
    posted_on_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner} - {self.bird_sighted} - {self.sighted_at_datetime}"
