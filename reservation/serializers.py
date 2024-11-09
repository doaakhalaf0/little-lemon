from rest_framework.serializers import ModelSerializer
from .models import Booking, Menu
class BookingSerializer:
    class Meta:
        model = Booking
        fields = "all"

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'