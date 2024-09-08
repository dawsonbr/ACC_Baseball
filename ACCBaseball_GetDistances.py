import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut
import time

# Load data
df = pd.read_excel('ACC_players.xlsx')

# Initialize the geocoder
geolocator = Nominatim(user_agent="geo_distance_calculator")

# Function to get coordinates from address 
def get_coordinates(address, retries=3):
    for _ in range(retries):
        try:
            location = geolocator.geocode(address)
            if location:
                return (location.latitude, location.longitude)
            else:
                return None
        except GeocoderTimedOut:
            time.sleep(1)  
    return None

# Calculate distances
distances = []
for _, row in df.iterrows():
    hometown_address = row['Hometown']
    university_address = row['University']
    
    hometown_coords = get_coordinates(hometown_address)
    university_coords = get_coordinates(university_address)
    
    if hometown_coords and university_coords:
        distance = geodesic(hometown_coords, university_coords).miles
        distances.append(distance)
    else:
        distances.append(None)

df['Distance (miles)'] = distances

# Save to Excel
df.to_excel('ACC_players_with_distances.xlsx', index=False)

