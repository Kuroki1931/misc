from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register('pdf', views.PDFViewSet)
router.register('company', views.CompanyViewSet)
router.register('question', views.QuestionViewSet)
router.register('ask', views.AskViewSet)

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('', include(router.urls)),
    url(r'^save-stripe-info/$', views.save_stripe_info),
]