from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    if "city" in request.POST:
        city = request.POST['city']
    else:
        # default city
        city = "kathmandu"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=15e1ac64e5bd4b5c33bb461750019511"
    # to convert kelvin to celsius
    param={'unit':'metric'}
    data=requests.get(url,param).json()
    temp=data['main']['temp']
    icon=data['weather'][0]['icon']
    description=data['weather'][0]['description']
    speed=data['wind']['speed']
    humidity=data['main']['humidity']
    pressure=data['main']['pressure']
    visibility=data['visibility']
    min_weather=data['main']['temp_min']
    max_weather=data['main']['temp_max']
    condition=data['weather'][0]['main']

    # context to send data to html
    context={
        'temp': f"{temp - 273:.2f}", 
        'city':city,
        'icon':icon,
        'description':description,
        'speed':speed,
        'humidity':humidity,
        'pressure':pressure,
        'visibility':visibility,
        'min_weather':f"{min_weather - 273:.2f}",
        'max_weather':f"{max_weather - 273:.2f}",
        'condition':condition,



    }
    return render(request, 'index.html', context)
