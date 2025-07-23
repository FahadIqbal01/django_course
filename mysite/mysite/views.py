# I have created this file - Fahad Iqbal
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request= request, template_name= 'index.html')

def analyze(request):
    # Check checkboxes values
    django_remove_punc = request.GET.get('remove_punc', 'off')
    django_full_caps = request.GET.get('full_caps', 'off')
    django_newline_remover = request.GET.get('newline_remover', 'off')
    django_extra_space_remover = request.GET.get('extra_space_remover', 'off')
    django_characters_count = request.GET.get('characters_count', 'off')
    
    # Get text to be analyzed
    django_text = request.GET.get('text', 'default')

    if django_remove_punc == 'on':
        punctuations = '''!()-[]{};:'"\,.<>./?@#$%^&*_~'''
        clean_text = ''
        for char in django_text:
            if char not in punctuations:
                clean_text = clean_text + char

        params = {'purpose' : 'Remove Punctutations', 'analyzed_text' : clean_text}
        return render(request= request, template_name= 'analyze.html', context= params)
    elif django_full_caps == 'on':
        clean_text = ''
        for char in django_text:
            clean_text = clean_text + char.upper()

        params = {'purpose' : 'Changed to Uppercase', 'analyzed_text' : clean_text}
        return render(request= request, template_name= 'analyze.html', context= params)
    elif django_newline_remover == 'on':
        clean_text = ''
        for char in django_text:
            if char != '\n':
                clean_text = clean_text + char
        
        params = {'purpose' : 'New Line Removed', 'analyzed_text' : clean_text}
        return render(request= request, template_name='analyze.html', context= params)
    elif django_extra_space_remover == 'on':
        clean_text = ''
        for index, char in enumerate(django_text):
            if django_text[index] == ' ' and django_text[index + 1] == ' ':
                pass
            else:
                clean_text = clean_text + char
        
        params = {'purpose' : 'Extra Spaces Removed', 'analyzed_text' : clean_text}
        return render(request= request, template_name= 'analyze.html', context= params)
    elif django_characters_count == 'on':
        characters_count = len(django_text)
        params = {'purpose' : 'Characters Count', 'analyzed_text' : characters_count}
        return render(request= request, template_name= 'analyze.html', context= params)
    else:
        return HttpResponse(content= 'Error')