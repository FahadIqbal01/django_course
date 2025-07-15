# I have created this file - Fahad Iqbal
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Fahad Iqbal!!")

def about(request):
    return HttpResponse("About Fahad Iqbal...")

def remove_punc(request):
    return HttpResponse("Remove Punctuation")

def capitalize_first(request):
    return HttpResponse('Capitalize First')

def new_line_remove(request):
    return HttpResponse('New Line Remove')

def space_remove(request):
    return HttpResponse('Space Remove')

def char_count(request):
    return HttpResponse('Characters Count')