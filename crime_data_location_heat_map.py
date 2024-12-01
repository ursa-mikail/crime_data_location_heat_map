import folium
from folium.plugins import HeatMap
import pandas as pd
import datapane as dp

# Load the crime data
data_file_path = '/content/sample_data/Crime_Data_from_2020_to_Present.csv'
crime_data = pd.read_csv(data_file_path)  # Make sure your file has latitude and longitude columns

# Initialize a map centered around the average latitude and longitude
crime_map = folium.Map(location=[crime_data['LAT'].mean(), crime_data['LON'].mean()], zoom_start=12)

# Prepare the data for the heatmap (just LAT and LON columns)
crime_locations = crime_data[['LAT', 'LON']].values

# Add the HeatMap layer to the map
HeatMap(crime_locations).add_to(crime_map)

# Save the map to an HTML file (optional)
crime_map.save("crime_heatmap.html")

# Display the map using Datapane
dp.Plot(crime_map)

