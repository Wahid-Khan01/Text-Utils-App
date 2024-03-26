# I have created this file views.py ---(Wahid)
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h1>Hello Wahid<h1> <a href=https://chat.openai.com/>ChatGPT</a><br><a href=https://www.youtube.com/>Youtube</a><br> <a href=https://getbootstrap.com/>Bootstrap</a><br><a href=https://replit.com/>Replit</a><br><a href=https://mail.google.com/>Gmail</a>")
def index(request):
    params = {'name':'Wahid', 'place':'Mumbai'}
    return render(request, 'index.html' , params)
# def about(request):
#     return HttpResponse("About Wahid")
# def newliner(request):
#     return HttpResponse("New Liner <br><a href=\><--</a>")
# def capfirst(request):
#     return HttpResponse("Cap First <br><a href=\><--</a>")
# def spacremov(request):
#     return HttpResponse("Space Remove <br><a href=\><--</a>")
# def puncremov(request):
#     # Get the Text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("Punc Remove <br><a href=\><--</a>")



def analyze(request):
# Get the Text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    
    if (removepunc == "on"):
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
# Analyze the text
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (uppercase == 'on'):
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
# Analyze the text
        params = {'purpose':'Made Text in UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
# Analyze the text
        params = {'purpose':'New Line removed from the Text', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' ') :
                analyzed = analyzed + char
# Analyze the text
        params = {'purpose':'Extra Space removed from the Text', 'analyzed_text': analyzed}

        # return render(request, 'analyze.html', params)
    if charcounter == 'on':
        analyzed = f'{djtext} \nand the total characters are {len(djtext)}'
# Analyze the text
        params = {'purpose':'Extra Space removed from the Text', 'analyzed_text': analyzed}
    
    if (removepunc!='on' and newlineremover!='on' and charcounter!='on' and extraspaceremover!='on' and uppercase!='on'):
        return HttpResponse('Error')
    
    return render(request, 'analyze.html', params)

def contact(request):
    return render(request, 'contact.html')

