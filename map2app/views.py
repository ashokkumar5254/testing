from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import coordinates_model
from .forms import *
import folium

def home(request):
    coordinates = coordinates_model.objects.all()
    form = CoordinatesForm()
    if request.method == 'POST':
        form = CoordinatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("map")
    context = {
    'coordinates': coordinates,
    'form' : form,
        }
    return render(request, 'home.html', context)

def maps(request):
   coordenadas = coordinates_model.objects.all().last()
   #list(coordinates_model.objects.values_list('lat','lon'))[-1]
   if coordenadas :
       lat=coordenadas.lat
       lon=coordenadas.lon
       print(lat)
       print(lon)
       map = folium.Map(Location=[lat,lon])
       folium.Marker([lat,lon]).add_to(map)
       folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
       folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
       folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
       folium.LayerControl().add_to(map)
       map = map._repr_html_()
       context = {'map': map}
       return render(request, 'maps.html', context)
   else:
       return HttpResponse('No co-ordinates')


# Create your views here.
