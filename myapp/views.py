from datetime import date
from django.shortcuts import render #type:ignore
from django.template import loader #type:ignore
from.models import Read #type:ignore
from django.http import HttpResponse #type:ignore
import json                #type:ignore
import urllib.request #type:ignore

def pagehtml(request):
    id=loader.get_template('user.html')
    return HttpResponse(id.render())
def pagehtmll(request):
    id=loader.get_template('user1.html')
    return HttpResponse(id.render())
def index(request):
    if request.method=='POST':
        appid='425cef233e19bf5877bbcddf306425ee'
        city=request.POST['city']
        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={425cef233e19bf5877bbcddf306425ee}').read()
        list_of_data=json.load(source)
        data={
            'country_code':str(list_of_data['sys']['country']),
            'coordinate':str(list_of_data['coord']['lon'])+''+str(list_of_data['coord']['lat']),
            'temp':str(list_of_data['main']['temp'])+'k',
            'pressure':str(list_of_data['main']['pressure']),
            'humidity':str(list_of_data['main']['humidity']),
        }
        print(data)
        return render(request,'user1.html',data)
    else:
        data={}
        return render(request,'user.html',data)
def area(request):
    if request.method=='POST':
        city=request.POST['city']
    else:
        city='london'
        apikey='f3fad9dded95b786e206e7f4f44a84cf'
        urlpost='https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={f3fad9dded95b786e206e7f4f44a84cf}'
        response=request.GET.get(urlpost)
        weather_data=response()
        context={
            'city':city,'temperature':weather_data['lat']['lon'],'description':
            weather_data['weather'][0]['description'],
            'icon':weather_data['weather'][0]['icon'],
        }
        return render(request,'user.html',context)

    
  
    

    

