# I have created this file - Fahad Iqbal
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Fahad Iqbal!!")

def about(request):
    return HttpResponse("About Fahad Iqbal...")