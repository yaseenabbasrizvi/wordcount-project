from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist= fulltext.split()
    worddictoinary={}
    for word in wordlist:
        if word in worddictoinary:
            #increase
            worddictoinary[word] +=1
        else:
            #add to the dictionary
            worddictoinary[word]=1
    sortedwords=sorted(worddictoinary.items(), key=operator.itemgetter(1), reverse= True)



    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedwords':worddictoinary.items()})
def about(request):
    return render(request, 'about.html')
