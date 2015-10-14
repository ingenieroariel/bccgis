from django.shortcuts import render
from django.http import HttpResponse
from osm.models import Bank

def index(request):
    html = '<html><body>Hello Bangladesh</body></html>'
    return HttpResponse(html)

def banks(request):
    html = '<html><body>'
    html += '<h1>List of banks</h1>'
    html += '<ol>'

    for bank in Bank.objects.all():
        # We do not want to display the banks with no name.
        if bank.name is None:
            continue

        # Add the bank's name and location to the webpage.
        html += '<li>%s: (%s, %s)</li>' % (bank.name, bank.geom.x, bank.geom.y)

    html += '</ol></body></html>'
    return HttpResponse(html)
