from django.db import models

class WeatherRecord(models.Model):
    date = models.DateField()
    max_temperature = models.FloatField(null=True, blank=True)
    min_temperature = models.FloatField(null=True, blank=True)
    precipitation = models.FloatField(null=True, blank=True)
    station_id = models.CharField()

    class Meta:
        unique_together = ('date', 'station_id')  

class YearlyStats(models.Model):
    year = models.IntegerField()
    station_id = models.CharField()
    avg_max_temperature = models.FloatField(null=True, blank=True)
    avg_min_temperature = models.FloatField(null=True, blank=True)
    total_precipitation = models.FloatField(null=True, blank=True)

    class Meta:
        managed = False
