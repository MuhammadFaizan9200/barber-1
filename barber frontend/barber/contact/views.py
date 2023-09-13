from django.shortcuts import render

# Create your views here.
def contact(request):
    context = {}
    template = "contact-us.html"
    return render(request, template, context)