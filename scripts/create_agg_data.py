
from django.db import connection
raw_query = "create or replace view weather_yearlystats as select  max(id) as id,date_part('year', date) as year,station_id,avg(max_temperature) as avg_max_temperature,avg(min_temperature) as avg_min_temperature,sum(precipitation) as total_precipitation from public.weather_weatherrecord  group by year,station_id"
cursor = connection.cursor()
cursor.execute(raw_query)
cursor.fetchall()
