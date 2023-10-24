from django.shortcuts import render
import json 
import urllib.request


# Create your views here.
def index(request): 
	if request.method == 'POST': 
		city = request.POST['city']
		print('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=4fe150f1bbd10a33e095419d83170202' )
		
		 
	
		res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=4fe150f1bbd10a33e095419d83170202' ).read()
		json_data = json.loads(res)
		data = {
			"city": city,
			"country_code": str(json_data['sys']['country']),
			'coordinate': str(json_data['coord']['lon']) + ' ' + 
			str(json_data['coord']['lat']),
			"temp": str(json_data['main']['temp'] + 'k'),
			"pressure": str(json_data['main']['pressure']),
			'humidiy': str(json_data['main']['humidity'])
		}
 


	else:
		data = {}



	return render(request, 'index.html', data)