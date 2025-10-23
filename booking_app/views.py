from django.shortcuts import render
from booking_app.models import Room

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }

    return render(request, 'home.html', context)