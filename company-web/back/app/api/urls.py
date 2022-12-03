from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import CompanyViewSet

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]