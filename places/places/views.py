from .models import Place
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_variable(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    variables = r.json()
    for variable in variables:
        if data["variable"] == variable["id"]:
            return True
    return False

def PlaceList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def PlaceCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_variable(data_json) == True:
            place = Place()
            place.variable = data_json['variable']
            place.value = data_json['name']
            measurement.save()
            return HttpResponse("successfully created place")
        else:
            return HttpResponse("unsuccessfully created place. Variable does not exist")

def PlacesCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        place_list = []
        for palce in data_json:
                    if check_variable(place) == True:
                        db_place = Place()
                        db_place.variable = measurement['variable']
                        db_place.name = measurement['name']
                        place_list.append(db_place)
                    else:
                        return HttpResponse("unsuccessfully created place. Variable does not exist")
        
        Measurement.objects.bulk_create(place_list)
        return HttpResponse("successfully created places")
