from utils.Coordinate import Coordinate
from utils.DataFilter import RainDataFilter
from utils.File import CSVFile

# rain data from .
# https://coastwatch.pfeg.noaa.gov/erddap/griddap/chirps20GlobalPentadP05.html
# used dataset:
# https://coastwatch.pfeg.noaa.gov/erddap/griddap/chirps20GlobalPentadP05.csv?precip%5B(2021-8-01T00:00:00Z):1:(2021-11-26T00:00:00Z)%5D%5B(30.0):.25:(42.0)%5D%5B(-123.0):.25:(-113.0)%5D

# Read data from file
input_file = CSVFile('chirps20GlobalPentadP05_1da0_1624_398c.csv')
rain_data = input_file.read()
if rain_data is None:
    exit(1)  # exit with error code 1

# Get coordinates of the city
input_city = str(input("Enter city name:[San Jose] ").strip() or "San Jose")
c_lat, c_lon = Coordinate.get_coordinate_of_city_from_internet(input_city)
if c_lat is None or c_lon is None:
    exit(1)  # exit with error code 1

# Get distance and rain threshold
try:
    dist_thresh = float(input("Enter distance threshold:[0.05] ").strip() or "0.05")
    rain_thresh = float(input("Enter rain threshold:[8.0] ").strip() or "8.0")
except ValueError:
    print("Invalid input")
    exit(1)

# Filter data
rain_data_filter = RainDataFilter(distance_threshold=dist_thresh, rain_threshold=rain_thresh, data=rain_data)
dates = rain_data_filter.get_results_from_data(coordinate_latitude=c_lat, coordinate_longitude=c_lon)

# Print results
for item in dates:
    print(item)
print("number of rainy 5-days: " + str(len(dates)))
