from django.shortcuts import render

# Create your views here.
def business(request):
    context = {}
    template = "business-page.html"
    return render(request, template, context)


