from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from eatgf.apps.locations.views import LocationList, LocationDetail
from eatgf.apps.restaurants.views import RestaurantDetail

from eatgf.libs.strict_slug import STRICT_SLUG_RE as SLUG_RE

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', RedirectView.as_view(url='/1/', permanent=False)),

    # url(r'^(?P<location>(' + SLUG_RE + ')/$',
    #    RedirectView.as_view(url=reverse('location-detail'), permanent=True))

    url(r'^$', TemplateView.as_view(template_name='index.html')),

    url(r'^locations/$',
        LocationList.as_view(),
        name='location-list'),

    url(r'^gluten-free-restaurants-in-(?P<slug>' + SLUG_RE + ')/',
        LocationDetail.as_view(),
        name='location-detail'),

    url(r'^(?P<location>' + SLUG_RE + ')/'
        '(?P<slug>' + SLUG_RE + ')-restaurant/',
        RestaurantDetail.as_view(),
        name='restaurant-detail'),
]
