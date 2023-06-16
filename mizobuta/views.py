from django.shortcuts import render
from django.contrib import admin
from .models import Prefecture, DangerousLocation
import geojson
import folium
from folium.plugins import HeatMap

def index(request):
    return render(request, 'index.html',)
    if request.method == 'POST':
        return redirect('main_page')

    return render(request, 'index.html')

def main_page(request):


    dangerous_locations = DangerousLocation.objects.filter(is_dangerous=True).select_related('city')
    num_dangerous_locations = dangerous_locations.count()
    prefectures = Prefecture.objects.all()

    context = {
        'num_dangerous_locations': num_dangerous_locations,
        'dangerous_locations': dangerous_locations,
        'prefectures': prefectures,
    }

    return render(request, 'main_page.html', context)
