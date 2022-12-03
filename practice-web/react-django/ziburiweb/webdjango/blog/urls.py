from django.urls import path, include
from blog import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.MemoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create', views.CreateMemo.as_view(), name='create'),
]