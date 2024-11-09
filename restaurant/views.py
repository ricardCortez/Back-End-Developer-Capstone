from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer

def index(request):
    return render(request, 'index.html', {})

# View for listing all menu items and creating a new one (GET and POST methods)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()  # Fetch all MenuItem records
    serializer_class = MenuItemSerializer  # Serializer to convert data to JSON format

# View for retrieving, updating, and deleting a single menu item (GET, PUT, DELETE methods)
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()  # Fetch all MenuItem records
    serializer_class = MenuItemSerializer  # Serializer to convert data to JSON format

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer