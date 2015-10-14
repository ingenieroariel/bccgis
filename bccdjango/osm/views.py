from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = '<html><body>Hello Bangladesh</body></html>'
    return HttpResponse(html)

def banks(request):
    html = '<html><body>This is the list of banks</body></html>'
    return HttpResponse(html)
