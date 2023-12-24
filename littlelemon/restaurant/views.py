from rest_framework.decorators import api_view
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated] 
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 