from django.views.generic import DetailView

from ..models import Restaurant


class RestaurantDetail(DetailView):
    template_name = "restaurants/restaurant_detail.html"

    def get_queryset(self):
        return Restaurant.objects.filter(
            location__slug=self.kwargs['location'])
