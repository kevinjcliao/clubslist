from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Club

def hello_world(request):
    clubs_list = Club.objects.order_by('name')
    output = ', '.join([c.name for c in clubs_list])
    template = loader.get_template('clubs/index.html')
    context = {
        'clubs_list': clubs_list
    }
    return HttpResponse(template.render(context, request))
