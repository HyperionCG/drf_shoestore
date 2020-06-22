from django.conf.urls import include, url

from api.views import ManufacturerViewSet, ShoeTypeViewSet, ShoeColorViewSet, ShoeViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet, basename='manufacturer')
router.register(r'shoe_type', ShoeTypeViewSet, basename='shoe_type')
router.register(r'shoe_color', ShoeColorViewSet, basename='shoe_color')
router.register(r'shoe', ShoeViewSet, basename='shoe')

urlpatterns = [
    url(r"^api/", include(router.urls))
]
