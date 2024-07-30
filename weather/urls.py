from django.urls import path
from .views import weather,weather_stats

urlpatterns = [
    path('weather/<str:date>/<str:station_id>', weather, name='weather'),
    path('weather/stats/<int:year>/<str:station_id>', weather_stats, name='weather stats')
]
