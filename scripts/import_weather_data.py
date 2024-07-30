import os
from datetime import datetime
from django.conf import settings
from weather.models import WeatherRecord


files_directory = os.path.join(settings.BASE_DIR, './wx_data/')  # Replace with your actual path
files = os.listdir(files_directory)
start_time = datetime.now()
total_records = 0    
for file_name in files:
    with open(os.path.join(files_directory, file_name), 'r') as file:  # Replace with your file path
        for line in file:
            total_records += 1
            parts = line.strip().split('	  ')
            if len(parts) == 4:
                try:
                    date_str = parts[0]
                    max_temp = float(parts[1]) / 10.0
                    min_temp = float(parts[2]) / 10.0
                    precip = float(parts[3]) / 10.0
                    date = datetime.strptime(date_str, '%Y%m%d').date()

                    # Save to database
                    weather_record = WeatherRecord(
                        date=date,
                        max_temperature=max_temp,
                        min_temperature=min_temp,
                        precipitation=precip,
                        station_id=file_name.split('.')[0]
                    )
                    weather_record.save()

                except Exception as e:
                    print(f"Error processing line in file {file_name}: {line}")
                    print(e)
end_time = datetime.now()
print(f'Ingestion completed. Total records ingested: {total_records}. Time taken: {end_time - start_time}')