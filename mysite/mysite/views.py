# I have created this file - Fahad Iqbal
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request= request, template_name= 'index.html')
    # return HttpResponse("Hello Fahad Iqbal!!")

def about(request):
    return HttpResponse("About Fahad Iqbal...")

def remove_punc(request):
    # Get the text from the form.
    django_text = request.GET.get('text', 'default')
    print(django_text)
    return HttpResponse("Remove Punctuation")

def capitalize_first(request):
    return HttpResponse('Capitalize First')

def new_line_remove(request):
    return HttpResponse('New Line Remove')

def space_remove(request):
    return HttpResponse('Space Remove')

def char_count(request):
    return HttpResponse('Characters Count')