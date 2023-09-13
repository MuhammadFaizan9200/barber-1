from django.urls import path

from . import views

urlpatterns = [
    path('', views.service, name='service'),
    path('service_booking/', views.service_booking, name='service-booking'),
    path('single_service/', views.single_service, name='single-service'),


]