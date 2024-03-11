from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VesselViewSet
from .views import VesselScheduleViewSet
from .views import BillOfLadingViewSet
from .views import ContainerViewSet

router = DefaultRouter()
router.register(r'vessels', VesselViewSet)
router.register(r'vessel_schedules', VesselScheduleViewSet)
router.register(r'bill_of_ladings', BillOfLadingViewSet)
router.register(r'containers', ContainerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]