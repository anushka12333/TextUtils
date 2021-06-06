from django.http import HttpResponse
from django.shortcuts import render



def pipe(request):
    params={'name':'ANK','place':'Purnea'}
    return render(request, 'index.html',params)

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline=request.POST.get('newline','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    counterchar=request.POST.get('counterchar','off')
    if (removepunc == "on"):
        punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Removed Punctuations','analyze_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        params={'purpose':'Changed To Uppercase','analyze_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)   
    if(newline=='on'):
        analyzed=""
        for char in djtext:
            if (char !="\n"):
                analyzed+=char
        params={'purpose':'Remove Newline','analyze_text':analyzed}
        # return render(request,'analyze.html',params)  
        djtext=analyzed

    if(extraspaceremover=='on'):
            analyzed=""
            for index,char in enumerate(djtext):
                if (djtext[index] == " " and djtext[index+1] == " "):
                    pass
                else:
                    analyzed+=char
            params={'purpose':'Remove extra space','analyze_text':analyzed}
            # return render(request,'analyze.html',params)   
            djtext=analyzed
                         
    if(counterchar=='on'):
            analyzed=0
            for char in djtext:
                if (char==" "):
                    pass
                else:
                    analyzed+=1
            params={'purpose':'Count the characters','analyze_text':analyzed}
            djtext=analyzed
    return render(request,'analyze.html',params)    
    # return render(request,'analyze.html',params)            
   
# def removepunc(request):
#     # print(request.GET.get('text','default'))
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("remove punc <a href='/'>back</a>")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("capitalize first")


# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount ")

