from webhook.models import Classes
import json
from icecream import ic


def run():
    with open('webhook/json/classes.json') as f:
        classes = json.load(f)
        # ic(classes)
        for num in classes:
            course = classes[num]
            # ic(course, type(course))
            class_ = Classes(name=course['name'],
                             course_num=course['number'],
                             course_description=course['desc'],
                             workload=float(course['workload']))
            class_.save()

