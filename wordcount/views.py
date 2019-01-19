from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text=request.GET['full_text']
    words = text.split()
    count_words = {}

    for i in words:
        if i in count_words:
            count_words[i] += 1
        else:
            count_words[i] = 1
    return render(request,'result.html',{'full':text, 'text_len':len(words),'count':count_words,'count_dict':count_words.items()})

    