from django.db import models

class BirdSighting(models.Model):
    species = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    date_seen = models.DateField()
    picture = models.ImageField(upload_to='bird_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.species} sighting at {self.location}"
