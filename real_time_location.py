# real_time_location.py
import random

def get_real_time_location():
    latitude = round(random.uniform(-90, 90), 5)
    longitude = round(random.uniform(-180, 180), 5)
    return latitude, longitude

# Example usage
cabs = {
    "cab1": get_real_time_location(),
    "cab2": get_real_time_location(),
    "cab3": get_real_time_location(),
}
