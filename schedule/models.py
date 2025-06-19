from django.db import models

# Create your models here.
class Schedule(models.Model):
    game_date = models.DateTimeField()
    # time = models.TimeField()
    opponent = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    home_game = models.BooleanField(default=True)


    def __str__(self):
        return f"Clique Mamabas Vs {self.opponent} on {self.game_date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['game_date']