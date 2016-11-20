from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import csv
import json
from django.core import serializers

# Create your views here.

def index(request):
    return HttpResponse('hello')



def report(request):
    inputs = request.POST
    print(User.objects.filter(id=inputs.get('name')).all())
    name = inputs.get('name')
    os = inputs.get('os')
    result = {'name':name, 'os':os}
    data = serializers.serialize('json', User.objects.filter(id=inputs.get('name')))
    return HttpResponse(data)
    # return HttpResponse(json.dumps(result))

def userConfirmation(request):
    inputs = request.GET
    print(len(serializers.serialize('json', Infomation.objects.filter(id=inputs.get('id')))))
    if len(serializers.serialize('json', Infomation.objects.filter(id=inputs.get('id')))) != 2:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

# def some_view(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
#
#     writer = csv.writer(response)
#     writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
#     writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
#
#     return response

