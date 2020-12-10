from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyse(request):
    djtext = request.POST.get('text','default')

    # Check checkbox Values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    # Giving Variables
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Check which checkbox is on

    if removepunc=="on":
        analysed = ""
        for i in djtext:
            if i not in punctuations:
                analysed = analysed + i
        params = {'purpose': 'Analysed Result-', 'analysed_text': analysed}
        djtext = analysed

    if fullcaps=="on":
        analysed = ""
        for i in djtext:
            analysed += i.upper()
        params = {'purpose': 'Analysed Result-', 'analysed_text': analysed}
        djtext = analysed

    if newlineremover=="on":
        analysed = ""
        for i in djtext:
            if i != "\n" and i != "\r":
                analysed = analysed + i
        params = {'purpose': 'Analysed Result-', 'analysed_text': analysed}
        djtext = analysed

    if extraspaceremover=="on":
        analysed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analysed = analysed + str(char)
        params = {'purpose': 'Analysed Result-', 'analysed_text': analysed}
        djtext = analysed

    if charcount == "on":
        analysed = ""
        l=len(djtext)
        analysed=str(l)
        params = {'purpose': 'No. of characters- after analysis', 'analysed_text': analysed}
        djtext = analysed

    else:
        analysed=''
        params = {'purpose': 'No option Selected', 'analysed_text': analysed}

    return render(request, 'analyse.html', params)
