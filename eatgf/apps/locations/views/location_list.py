from django.views.generic import ListView

from ..models import Location


class LocationList(ListView):
    template_name = "locations/location_list.html"
    model = Location
