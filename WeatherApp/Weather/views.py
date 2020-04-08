from typing import Dict, List, Any, Union

import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=b44d498b6b4dba2ee5ce1f9f051a0696'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city.info = {
            "city": city.name,
            "temp": res["main"]["temp"],
            "icon": ["weather"][0]["icon"]
        }

        all_cities.append(city.info)

    context = {'all info': all_cities, 'form': form}

    return render(request, 'index.html', context)
