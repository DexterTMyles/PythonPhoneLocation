import phonenumbers
from phonenumbers import geocoder
import folium
from test import number


check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")

print(number_location)