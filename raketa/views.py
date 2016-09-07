from django.shortcuts import render

#def index(request):
#    return HttpResponse("Hello, world")

def home(request):
    return render(request, "main.html")
