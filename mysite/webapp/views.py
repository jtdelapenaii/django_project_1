from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>HEY SENTDEX! THIS IS NOW CLONED WITH GITHUB</h2>")
