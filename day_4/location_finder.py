from geopy.geocoders import Nominatim
# geopy.geocoders abstracting the service's API.
geolocate = Nominatim(user_agent="distance_calc")
# user inputs longitude and latitude
longitude = str(input("enter longitude"))
latitude = str(input("enter latitude"))
locates = latitude + "," + longitude
# "52.509669-la, 13.376294-lo" sample data
# reverse gets raw data
location = geolocate.reverse(locates)
print(location.address)
print((location.latitude, location.longitude))

