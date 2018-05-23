from django.test import TestCase
from .models import City
from .models import Hotel
from .filehandler import *

# Create your tests here.

city_path = "/home/theophile/TPS/2A/Stage/Maykin_Assignment/maykin/files/city_test.csv"
hotel_path = "/home/theophile/TPS/2A/Stage/Maykin_Assignment/maykin/files/hotel_test.csv"

class HotelTestCase(TestCase):
    def setUp(self):

        cities = import_csv_from_file(city_path)
        for row in cities:
            City.objects.create(cityID=row[0], name=row[1])  

        hotels = import_csv_from_file(hotel_path)
        for row in hotels:
            Hotel.objects.create(cityID=row[0], hotelID = row[1], name=row[2])


    def test_city(self):        

        self.assertEqual(City.objects.get(cityID="STR").name, "Strasbourg")
        self.assertEqual(City.objects.get(cityID="BRE").name, "Brest")


    def test_hotels(self):

        self.assertEqual(Hotel.objects.get(hotelID="BRE02").name, "Hôtel Kyriad Brest Centre")
        self.assertEqual(Hotel.objects.get(hotelID="STR01").name, "Le Lodge Hôtel Strasbourg")


    def test_hotel_list(self):
        strasbourg = City.objects.get(cityID="STR")
        brest = City.objects.get(cityID="BRE")

        hotels_strasbourg = list(Hotel.objects.filter(cityID=strasbourg.cityID))
        hotels_brest = list(Hotel.objects.filter(cityID=brest.cityID))

        self.assertEqual(hotels_strasbourg, [Hotel.objects.get(hotelID = "STR01"), Hotel.objects.get(hotelID = "STR02")])
        self.assertEqual(hotels_brest, [Hotel.objects.get(hotelID = "BRE01"), Hotel.objects.get(hotelID = "BRE02"), Hotel.objects.get(hotelID = "BRE03")])






