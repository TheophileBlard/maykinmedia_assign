from django.core.management.base import BaseCommand, CommandError

import requests
import csv

from hotels.models import Hotel
from hotels.models import City

user = 'python-demo'
password = 'claw30_bumps'

class Command(BaseCommand):
    help = 'Update City and Hotel models in DB'

    def add_arguments(self, parser):                
        parser.add_argument('url_city', nargs='+', type=str)
        parser.add_argument('url_hotel', nargs='+', type=str)
        parser.add_argument('mode', nargs='+', type=str)        

    def getList(self, url):        
        with requests.Session() as s:
            download = s.get(url, auth=(user, password))
            if (download.status_code == 401):
                return -1
            
            decoded = download.content.decode('utf-8')
            cr = csv.reader(decoded.splitlines(), delimiter=';')
            return list(cr)
           
    def getListFromLocalFiles(self, path):
        data=[]
        try:
            with open(path, 'r') as csvfile:            
                file = csv.reader(csvfile, delimiter=';')
                for row in file:
                    row_data = []
                    for dat in row:
                        row_data.append(dat)
                    data.append(row_data)
                    #data.append(', '.join(row))
            return data
        except:
            return -1

    def handle(self, *args, **options): 

        url_city = options['url_city'][0]
        url_hotel = options['url_hotel'][0]      
        
        if(options['mode'][0]=="local"):
            cityList = self.getListFromLocalFiles(url_city)
            hotelList = self.getListFromLocalFiles(url_hotel)
        
        else:
            cityList = self.getList(url_city)
            hotelList = self.getList(url_hotel)
                        
        
        if(cityList !=-1):            
            City.objects.all().delete()
            
            for row in cityList:
                newCity = City(ID = row[0], name = row[1])
                newCity.save()
            self.stdout.write(self.style.SUCCESS("Successfully loaded file '%s'" % url_city))

        else:
            self.stdout.write(self.style.ERROR("Couldn't download file '%s'" % url_city))  
             
        if(hotelList !=-1):            
            Hotel.objects.all().delete()
            
            for row in hotelList:
                #newHotel = Hotel(city = City.objects.filter(ID=row[0]), cityID = row[0], ID = row[1], name = row[2])
                newHotel = Hotel(cityID = row[0], ID = row[1], name = row[2])
                newHotel.save()
            self.stdout.write(self.style.SUCCESS("Successfully loaded file '%s'" % url_hotel))
        else:            
            self.stdout.write(self.style.ERROR("Couldn't download file '%s'" % url_hotel)) 