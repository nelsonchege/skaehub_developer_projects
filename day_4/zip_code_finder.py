from geopy.geocoders import Nominatim
# geopy.geocoders abstracting the service's API.
geolocate = Nominatim(user_agent="zip_code_finder")
# user input location/zip code
location_one = input("enter location/zip code:")
location = geolocate.geocode(location_one)
print("location/zip details")
# print all data
print(location.raw)
