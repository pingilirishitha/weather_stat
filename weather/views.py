from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WeatherRecord , YearlyStats
import datetime

@api_view(['GET'])
def weather(request, date,station_id):
    try:
        if not is_valid_date_format(date):
            return Response({'error': 'Invalid date format. Please use yyyy-mm-dd.'}, status=400)
        weather_data = WeatherRecord.objects.filter(date = date,station_id = station_id)
        data = {
            'weather_data': list(weather_data.values()),  # Convert QuerySet to list of dictionaries
        }
        return Response(data)
    except ValueError:
        return Response({'error': 'Invalid date format. Please use yyyy-mm-dd.'}, status=400)
    
@api_view(['GET'])
def weather_stats(request, year,station_id):
    try:
        if not is_4_digit_integer(year):
            return Response({'error': 'Invalid year format. Please use yyyy'}, status=400)
        weather_data = YearlyStats.objects.filter(year = year,station_id = station_id)
        data = {
            'weather_data': list(weather_data.values()),  # Convert QuerySet to list of dictionaries
        }
        return Response(data)
    except ValueError:
        return Response({'error': 'Invalid year format. Please use yyyy'}, status=400)




def is_valid_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    

def is_4_digit_integer(value):
    try:
        num = int(value)
        return 1000 <= num <= 9999
    except ValueError:
        return False