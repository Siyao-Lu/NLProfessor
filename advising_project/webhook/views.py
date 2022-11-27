from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from icecream import ic

# define home function
def home(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def webhook(request):
    """
    A bunch of if else loops that determine the logic.
    """
    # build a request object
    req = json.loads(request.body)
    # get action from json
    intent = req.get('queryResult').get('intent').get('displayName')
    params = req.get('queryResult').get('parameters')
    # The ugly part
    if intent == 'Get-Name' and len(params) == 2:
        create_student(params['name'], params['unique_name'])
    elif intent == 'Major' and len(params) == 2:
        add_major_year(params)
    ic(params, intent)

    # return a fulfillment message
    # fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}
    # # return response
    # return JsonResponse(fulfillmentText, safe=False)
    return None

def create_student(name, unique_name):
    stud = Student(name=name, unique_name=unique_name)
    stud.save()
    ic(Student.objects.all(), stud.id)

def add_major_year(params):
    stud = Student.objects.all()[0]
    stud.major = params['major']
    stud.year = params['year']
    stud.save()
