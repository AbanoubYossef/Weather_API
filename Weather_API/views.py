import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=37cabc761df71a3dcdfc36169911e4b8&q='

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']  # Get the city name from the form
            data_url = url + city_name
            try:
                response = requests.get(data_url).json()
                city_weather = {
                    "city": response['name'],
                    "icon": response['weather'][0]['icon'],  
                    "temperature": response['main']['temp'],
                    "description": response['weather'][0]['description'],
                    "feels_like": response['main']['feels_like'],
                    "humidity": response['main']['humidity'],
                    "pressure": response['main']['pressure'],
                    "max_temperature": response['main']['temp_max'],
                    "min_temperature": response['main']['temp_min'],
                    "visibility": response.get('visibility', 'N/A'),  # Handle visibility if it's not present
                    "time": response['dt'],  # Current time
                    "sunrise": response['sys']['sunrise'],  # Sunrise time
                    "sunset": response['sys']['sunset'],  # Sunset time
                }
                # Check if the city already exists in the database
                if not City.objects.filter(name=city_name).exists():
                # City does not exist, so save it
                # Save the city to the database
                    city = City(name=city_name)
                    city.save()
            except Exception as e:
                print(f"Error fetching data for {city_name}: {e}")
                city_weather = None
        else:
            city_weather = None
    else:
        form = CityForm()
        city_weather = None

    return render(request, 'weatherAPP.html', {'city_weather': city_weather, 'form': form})

    