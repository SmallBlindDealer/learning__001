

from datetime import datetime, timedelta
# import pandas as pd
import csv

# fare rules
fares = {
    ('Green', 'Green'): {'peak': 2, 'non_peak': 1, 'daily_cap': 8, 'weekly_cap': 55},
    ('Red', 'Red'): {'peak': 3, 'non_peak': 2, 'daily_cap': 12, 'weekly_cap': 70},
    ('Green', 'Red'): {'peak': 4, 'non_peak': 3, 'daily_cap': 15, 'weekly_cap': 90},
    ('Red', 'Green'): {'peak': 3, 'non_peak': 2, 'daily_cap': 15, 'weekly_cap': 90},
}

# peak hours
peak_hours = {
    'Monday': [(8, 10), (16, 19)],
    'Tuesday': [(8, 10), (16, 19)],
    'Wednesday': [(8, 10), (16, 19)],
    'Thursday': [(8, 10), (16, 19)],
    'Friday': [(8, 10), (16, 19)],
    'Saturday': [(10, 14), (18, 23)],
    'Sunday': [(18, 23)],
}


def is_peak(datetime_obj):
    day_name = datetime_obj.strftime('%A')
    hour = datetime_obj.hour
    for start, end in peak_hours.get(day_name, []):
        if start <= hour <= end:
            return True
    return False


def calculate_fare(from_line, to_line, datetime_obj, daily_total, weekly_total):
    key = (from_line, to_line)
    if key not in fares:
        return 0
    
    # check if peak or non-peak
    peak = is_peak(datetime_obj)
    fare_type = 'peak' if peak else 'non_peak'
    fare = fares[key][fare_type]
    
    # apply daily cap
    daily_cap = fares[key]['daily_cap']
    if daily_total + fare > daily_cap:
        fare = daily_cap - daily_total

    # apply weekly cap
    weekly_cap = fares[key]['weekly_cap']
    if weekly_total + fare > weekly_cap:
        fare = weekly_cap - weekly_total

    return fare

def process_trips(csv_file):
    daily_fares = {}
    weekly_fares = {}
    total_fare = 0

    # read CSV
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            from_line    = row[0].strip()
            to_line      = row[1].strip()
            datetime_str = row[2].strip()

            trip_time = datetime.fromisoformat(datetime_str)
            
            # Reset daily fare if it's a new day
            date_key = trip_time.date()
            if date_key not in daily_fares:
                daily_fares[date_key] = 0
            
            # Weekly key (week starting on Monday)
            week_key = date_key - timedelta(days=date_key.weekday())
            if week_key not in weekly_fares:
                weekly_fares[week_key] = 0
            
            # Calculate fare for this trip
            fare = calculate_fare(
                from_line, to_line, trip_time, 
                daily_fares[date_key], weekly_fares[week_key]
            )
            
            # Update daily and weekly totals
            daily_fares[date_key] += fare
            weekly_fares[week_key] += fare
            
            total_fare += fare

    return total_fare


print(process_trips('trips.csv'))
