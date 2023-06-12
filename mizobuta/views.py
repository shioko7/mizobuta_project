from django.shortcuts import render
from .models import HazardousLocation,Prefecture
from .models import City, DangerousLocation

def index(request):
    locations = HazardousLocation.objects.all().order_by('-count')
    return render(request, 'index.html', {'locations': locations})
    if request.method == 'POST':
        return redirect('main_page')

    return render(request, 'index.html')

def main_page(request):
    dangerous_locations = DangerousLocation.objects.filter(is_dangerous=True).select_related('city')
    num_dangerous_locations = dangerous_locations.count()

    context = {
        'num_dangerous_locations': num_dangerous_locations,
        'dangerous_locations': dangerous_locations,
    }

    return render(request, 'main_page.html', context)
