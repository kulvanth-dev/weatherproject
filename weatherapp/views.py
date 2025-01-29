from django.shortcuts import render 
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'


    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6c9aeb89c62d496fb8b20151ad2cd18a'
    PARAMS ={'units':'metric'}
    try:
        data =requests.get(url,PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()
        return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})
    except:
        messages.error(request,'entered city name is wrong')
        day=datetime.date.today()
        return render(request,'index.html',{'description':'error. city is not available in weather report.','day':day,'city':'city','exception_occured':True})
