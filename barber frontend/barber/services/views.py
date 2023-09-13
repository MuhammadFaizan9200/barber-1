from django.shortcuts import render
from base_models.models import Services

# Create your views here.
def service(request):
    context = {}
    services_data = Services.objects.all()
    context = {
        'services_data': services_data,
    }
    template = "service.html"
    return render(request, template, context)


# Create your views here.
def service_booking(request):
    context = {}
    template = "service-booking.html"
    return render(request, template, context)


# Create your views here.
def single_service(request):
    context = {}
    template = "single-service.html"
    return render(request, template, context)