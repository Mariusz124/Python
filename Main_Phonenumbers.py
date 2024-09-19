import phonenumbers
from phonenumbers import geocoder
#from Test_phonenumbers import number
import folium
key = "8e4221e72d1f4512b94ef39c754bd317"
number = input('Podaj numer telefonu z kodem kraju: ')
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "pl")
print(number_location)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"pl"))
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save("mylocation.html")