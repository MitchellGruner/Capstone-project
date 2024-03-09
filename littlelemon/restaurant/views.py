from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu

def index(request):
    return render(request, 'index.html', {})

class BookingViewSet (viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemsView (generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer