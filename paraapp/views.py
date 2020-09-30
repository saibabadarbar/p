from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    s='<h1>hello my first message</h1>'
    return HttpResponse(s)
