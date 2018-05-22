from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import City
from .models import Hotel

from .forms import CityForm

autocomplete = True

def get_city(request):
    
	if request.method == 'POST':

		if(autocomplete):
			
			try:
				city_id = City.objects.get(name=request.POST['city_name']).ID
				hotel_list = Hotel.objects.filter(cityID=city_id)
			except:
				hotel_list=[]
			return render(request, 'hotels_complete.html', {'hotel_list' : hotel_list})					

		else:

			form = CityForm(request.POST)
			if form.is_valid():				          
				return render(request, 'hotels.html', {'form': form, 'hotel_list' : Hotel.objects.filter(cityID=request.POST['city'])})		

	#If GET :
	if(autocomplete):
		return render(request, 'hotels_complete.html')
	else:
		form = CityForm()
		return render(request, 'hotels.html', {'form': form})


def get_cities(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        cities = City.objects.filter(name__icontains = q )[:30]
        results = []
        for city in cities:
            city_json = {}
            city_json['id'] = city.ID
            city_json['label'] = city.name
            city_json['value'] = city.name
            results.append(city_json)
        data = json.dumps(results)        
    else:
        data = 'fail'
    mimetype = 'application/json'
    print(data)
    return HttpResponse(data, mimetype)
