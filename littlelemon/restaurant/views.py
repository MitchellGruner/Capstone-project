from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu

def index(request):
    return render(request, 'index.html', {})

class BookingViewSet (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemsView (generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class SingleMenuItemView (generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]