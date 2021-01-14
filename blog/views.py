from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "blog/index.html")


def number(request, num):
    context = { 'number' : num }
    return render(request, "blog/number.html", context)

def posts(request):
    posts = [
        { 'title' : 'hiiii',
          'user' : 'lucca' },
        { 'title' : 'tsla go stonks',
          'user' : 'elon' },
        { 'title' : 'bedwars',
          'user' : 'quirino' },
    ]
    context = { 'posts' : posts }
    return render(request, "blog/posts.html", context)
