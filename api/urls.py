from django.conf.urls import include, url

from api.views import ManufacturerViewSet, ShoeTypeViewSet, ShoeColorViewSet, ShoeViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet)
router.register(r'shoe_type', ShoeTypeViewSet)
router.register(r'shoe_color', ShoeColorViewSet)
router.register(r'shoe', ShoeViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls))
]
