# from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Helloaaa World'
    context['world'] = 'hahahahaha'
    return render(request, 'hello.html', context)