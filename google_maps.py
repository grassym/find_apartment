# coding: utf-8
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

geolocator = Nominatim()
home = geolocator.geocode("львів home_text")
work = geolocator.geocode("львів work_text")
print(home.address)
print(work.address)

home_point = (home.latitude, home.longitude)
work_point = (work.latitude, work.longitude)
print(vincenty(home_point, work_point).meters)