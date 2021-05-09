from django.shortcuts import render
from django.http import HttpResponse
from wordquiz.models import Threequiz, Fourquiz, Fivequiz
import json
import random

def quiz_three(request, tag):
    entries = Threequiz.objects.get(tag=int(tag))
    data = entries.dic()
    letter = []
    name = list(data['name'])
    for i in range(9):
        letter.append(chr(random.randint(65,90)))
    letter.extend(name)
    random.shuffle(letter)
    data["letters"] = letter
    return HttpResponse(json.dumps(data), content_type="application/json")

def quiz_four(request, tag):
    entries = Fourquiz.objects.get(tag=int(tag))
    data = entries.dic()
    letter = []
    name = list(data['name'])
    for i in range(8):
        letter.append(chr(random.randint(65,90)))
    letter.extend(name)
    random.shuffle(letter)
    data["letters"] = letter
    return HttpResponse(json.dumps(data), content_type="application/json")

def quiz_five(request, tag):
    entries = Fivequiz.objects.get(tag=int(tag))
    data = entries.dic()
    letter = []
    name = list(data['name'])
    for i in range(7):
        letter.append(chr(random.randint(65,90)))
    letter.extend(name)
    random.shuffle(letter)
    data["letters"] = letter
    return HttpResponse(json.dumps(data), content_type="application/json")