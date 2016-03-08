from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Club

def hello_world(request):
    clubs_categories = Club.CATEGORY_CHOICES
    categorized_club_list = []
    clubs_size = 0
    there_are_clubs = False
    for x in range (0, len(clubs_categories)):
        print "hello world"
        category_id = clubs_categories[x][0]
        clubs_in_category = Club.objects.all().filter(category=category_id).order_by('name')
        categorized_club_list.append([clubs_categories[x][1], clubs_in_category])
        clubs_size += len(clubs_in_category)

    print categorized_club_list

    there_are_clubs = clubs_size > 0

    template = loader.get_template('clubs/index.html')
    context = {
        'clubs_list': categorized_club_list,
        'clubs_size': clubs_size,
        'there_are_clubs': there_are_clubs
    }
    return HttpResponse(template.render(context, request))
