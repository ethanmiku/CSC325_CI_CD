from django.urls import path
from booking.views import api_status
from booking.views import create_booking

urlpatterns = [path("api/bookings/", create_booking), 
               path("api/status/", api_status, name="api_status")]
