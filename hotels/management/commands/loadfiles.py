from django.core.management.base import BaseCommand, CommandError

from hotels.models import Hotel
from hotels.models import City

from hotels.filehandler import *


class Command(BaseCommand):
    help = 'Update City and Hotel models in DB'

    def add_arguments(self, parser):                
        parser.add_argument('url_city', nargs='+', type=str)
        parser.add_argument('url_hotel', nargs='+', type=str)
        parser.add_argument('mode', nargs='+', type=str)

    def handle(self, *args, **options): 

        url_city = options['url_city'][0]
        url_hotel = options['url_hotel'][0]      
        
        if(options['mode'][0]=="local"):
            cityList = import_csv_from_file(url_city)
            hotelList = import_csv_from_file(url_hotel)
        
        else:
            cityList = import_csv_from_url(url_city)
            hotelList = import_csv_from_url(url_hotel)
                        
        
        if(cityList !=-1):            
            City.objects.all().delete()
            
            for row in cityList:
                newCity = City(cityID = row[0], name = row[1])
                newCity.save()
            self.stdout.write(self.style.SUCCESS("Successfully loaded file '%s'" % url_city))

        else:
            self.stdout.write(self.style.ERROR("Couldn't download file '%s'" % url_city))  
             
        if(hotelList !=-1):            
            Hotel.objects.all().delete()
            
            for row in hotelList:
                #newHotel = Hotel(city = City.objects.filter(ID=row[0]), cityID = row[0], ID = row[1], name = row[2])
                newHotel = Hotel(cityID = row[0], hotelID = row[1], name = row[2])
                newHotel.save()
            self.stdout.write(self.style.SUCCESS("Successfully loaded file '%s'" % url_hotel))
        else:            
            self.stdout.write(self.style.ERROR("Couldn't download file '%s'" % url_hotel)) 