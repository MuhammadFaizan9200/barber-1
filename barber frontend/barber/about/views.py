from django.shortcuts import render

# Create your views here.
def about(request):
    context = {}
    template = "about-us.html"
    return render(request, template, context)