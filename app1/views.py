from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def messi(request):
    return HttpResponse('<h2>messi is goat</h2>')
