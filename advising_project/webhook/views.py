from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from icecream import ic
import os
from pathlib import Path

# directory reach
directory = os.path.dirname(__file__)

# setting path
from search.keyword_search import classes_db

report_res = {
    'name': '',
    'courses': [],
    'basedOn': [],
}
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
        report_res['name'] = params['name']
        report_res['courses'] = []
        report_res['basedOn'] = []
        # create_student(params['name'], params['unique_name'])
    elif intent == 'Major' and len(params) == 2:
        # add_major_year(params)
        report_res['basedOn'].append(params['major'])
        report_res['basedOn'].append(params['year'])
    elif intent == 'Show-Class' and len(params) == 1:
        # file = Path('webhook/json/report.json')
        # file.touch(exist_ok=False)
        # with open('webhook/json/report.json', 'r+') as f:
        #     prev_ = json.load(f)
        #     res = prev_.append(search_class(params['class']))
        #     ic(res)
        #     res_json = json.dumps(res, indent=4)
        #     f.write(res_json)
        report_res['courses'] += search_class(params['class'])
        report_res['basedOn'].append(params['class'])
    #     ic(report_res)
    # ic(params, intent)
    return None

def show_report(request):
    return HttpResponse(json.dumps(report_res))

def create_student(name:str, unique_name:str):
    stud = Student(name=name, unique_name=unique_name)
    stud.save()
    ic(Student.objects.all(), stud.id)

def add_major_year(params):
    stud = Student.objects.all()[0]
    stud.major = params['major']
    stud.year = params['year']
    stud.save()


def search_class(keywords: str, info: list=["number", "name", "desc", "workload"], db = None) -> list:
    """Search classes based on keywords.

    Input:
    keywords: string, i.e. "Machine Learning"
    info: list, info returned associated with each class in the returned list

    Output:
    A list consists of 6 relevant classes sorted by tf-idf score.
    """
    db = classes_db(db_file="webhook/json/classes.json")
    init_result = db.search(keywords)
    post_process = []
    for _dict in init_result:
        new_dict = {}
        for _key in info:
            new_dict[_key] = _dict[_key]
        new_dict['basedOn'] = [keywords]
        new_dict['courseDept'] = 'EECS'
        post_process.append(new_dict)
    return post_process

