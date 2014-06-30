from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from ..models import Location


class LocationDetail(SingleObjectMixin, ListView):
    """
    List all the restaurants for a given location.
    """

    template_name = "locations/location_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Location.objects.all())
        return super(LocationDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LocationDetail, self).get_context_data(**kwargs)
        context['location'] = self.object
        return context

    def get_queryset(self):
        return self.object.restaurants.all()
