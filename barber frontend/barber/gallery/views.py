from django.shortcuts import render

# Create your views here.
def gallery(request):
    context = {}
    template = "gallery.html"
    return render(request, template, context)