from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1fa2de3e0e9c440a806134b1c7f42686').read()
        json_data = json.loads(res)
        data = {
            'country_code':str(json_data['sys']['country']),
            'coordinate':str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp':str(json_data['main']['temp']) + 'k',
            'pressure':str(json_data['main']['pressure']),
            'humidity':str(json_data['main']['humidity']),
        }

    else:
        city = ''
        data= {}
    return render(request, 'index.html', {'city':city, 'data':data})