from geopy.geocoders import Nominatim

# geopy.geocoders abstracting the service's API.
geolocate = Nominatim(user_agent="countryFromState")

# enter the name of city
location_one = input("enter city:")
location = geolocate.geocode(location_one)
print("city and country is")
# prints city and country
print(location.address)
