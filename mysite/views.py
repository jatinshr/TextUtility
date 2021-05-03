from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')        
 
def analyze(request):
    
    djtext = request.POST.get('text','default')
    

    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    text = djtext
    analyze = ""
    purpose = ""
    if removepunc == 'on' or capitalize == 'on' or spaceremover == 'on' or newlineremover == 'on':

        if removepunc == 'on':
            purpose  += ' |Removed punctuation| '
            for char in djtext:
                if char not in punctuations:
                    analyze += char
            djtext = analyze
            analyze = ""

        if capitalize == 'on':
            purpose  += ' |Capitalize| '
            analyze = djtext.upper()
            djtext = analyze
            analyze = ""

        if spaceremover == 'on':
            purpose  += ' |Removing extra space| '
            for index, char in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index+1] == " "):
                    analyze += char
            djtext = analyze
            analyze = ""

        if newlineremover == 'on':
            purpose  += ' |Removing New Line| '
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyze += char
            djtext = analyze
            analyze = ""
            
        
        paramas = {'purpose':purpose, 'text':text, 'analyze':djtext}
        return render(request, 'analyze.html', paramas)
    else:
        return HttpResponse("Error")