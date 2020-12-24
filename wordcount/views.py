from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordcountdict = {}

    for word in wordlist:
        count
        if word in wordcountdict:
            # increment counter
            wordcountdict[word] += 1
        else:
            # add word to dictionary
            wordcountdict[word] = 1

    sorteddict = sorted(wordcountdict.items(),
                        key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sorteddict': sorteddict})


def about(request):
    return render(request, 'about.html')
