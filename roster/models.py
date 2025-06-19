from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    jersey_number = models.IntegerField(unique=True)
    height = models.DecimalField(max_length=10, blank=True, null=True, max_digits=1, decimal_places=1)  # e.g., '6\'2"'
    weight = models.DecimalField(max_length=10, blank=True, null=True, max_digits=1, decimal_places=1)
    image = CloudinaryField(
        'News Image',
        help_text="Player Image."
    ) 
    position = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[
            ('PG', 'Point Guard'),
            ('SG', 'Shooting Guard'),
            ('SF', 'Small Forward'),
            ('PF', 'Power Forward'),
            ('C', 'Center'),
        ]
    )


    class Meta:
        verbose_name_plural = "Players"
        ordering = ['jersey_number']

    def __str__(self):
        return f"{self.name} - #{self.jersey_number} ({self.position})"  