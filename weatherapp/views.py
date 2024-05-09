# from django.shortcuts import render
# import requests
# import datetime
# # Create your views here.


# def home(request):
#     if 'city' in requests.POST:
#         city=request.POST['city']
#     else:
#         city='indore'
#     url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e88519e9fe21c8a98d174e6374135473'
#     PARAMS={'units':'metric'}

#     data=request.get(url,PARAMS).json()
#     description=data['weather'][0]['description']
#     icon=data['weather'][0]['icon']
#     temp=data['main']['temp']
#     day=datetime.date.today()
#     return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day})

from django.shortcuts import render
import requests
import datetime
from django.contrib import messages

def home(request):
    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Mumbai'
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e88519e9fe21c8a98d174e6374135473'
    API_KEY='AIzaSyBqqOJVfN4U5tC5-DDzPhvftKLOKOvXwW8'
    SEARCH_ENGINE_ID='51d6fb788a22d44fe'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']



    params = {'units': 'metric'}  # Use a colon instead of a semicolon in the dictionary
    
    response = requests.get(url, params=params)

    try:
        data = requests.get(url,params).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()
        return render(request, 'index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day,'city':city,'exception_occured':False,'image_url':image_url})
    
    except KeyError:
        exception_occured=True
        messages.error(request,'Entered data is not availab;e to API')
        day=datetime.date.today()
        return render(request, 'index.html', {'description': 'Clear Sky', 'icon': '01d', 'temp': 25, 'day': day,'city':city,'exception_occured':True,'image_url':image_url})
