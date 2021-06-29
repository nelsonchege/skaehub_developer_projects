from geopy import Nominatim
from geopy.distance import geodesic
# geopy.geocoders abstracting the service's API.
geolocate = Nominatim(user_agent="zip_code_finder")
location_one = input("enter first location:")
location_two = input("enter second location:")
# this finds the locations using the method below
location1 = geolocate.geocode(location_one)
location2 = geolocate.geocode(location_two)
# saving the the longitude and latitude
loc1 = (location1.latitude, location1.longitude)
loc2 = (location2.latitude, location2.longitude)
# use to get the distance between the two location
distance = geodesic(loc1, loc2).km
print("the distance is: " + str(distance) + " km")
