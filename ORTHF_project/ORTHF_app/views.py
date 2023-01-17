from django.shortcuts import render
from rest_framework import viewsets
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum

from django.db import connection

import json

from ORTHF_app import models
from ORTHF_app import serializers
from ORTHF_app.models import Actions

class TypeEmployeeViewset(viewsets.ModelViewSet):
    serializer_class=serializers.TypeEmployeeSerializer
    queryset= models.TypeEmployee.objects.all()
class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class=serializers.EmployeeSerializer
    queryset= models.Employee.objects.all()

class PatientViewset(viewsets.ModelViewSet):
    serializer_class=serializers.PatientSerializer
    queryset= models.Patient.objects.all()

class ActionsViewset(viewsets.ModelViewSet):
    serializer_class=serializers.ActionsSerializer
    queryset= models.Actions.objects.all()

class WorkingTimeViewset(viewsets.ModelViewSet):
    serializer_class=serializers.WorkingTimeSerializer
    queryset= models.WorkingTime.objects.all()

class VisitsViewset(viewsets.ModelViewSet):
    serializer_class=serializers.VisitsSerializer
    queryset= models.Visits.objects.all()

class TypeWorkingViewset(viewsets.ModelViewSet):
    serializer_class=serializers.TypeWorkingSerializer
    queryset= models.TypeWorking.objects.all()

class RealWorkingTimeViewset(viewsets.ModelViewSet):
    serializer_class=serializers.RealWorkingTimeSerializer
    queryset= models.RealWorkingTime.objects.all()

class ConfigViewset(viewsets.ModelViewSet):
    serializer_class=serializers.ConfigSerializer
    queryset= models.Config.objects.all()

#def dovolena(request, pk):
    #if request.method== "GET":
      #  working_days = models.RealWorkingTime.values()
      #  return working_days

def suma(request, pk):
    if request.method== "GET":
        q = list(models.Actions.objects.filter(id=pk).aggregate(data=Sum("suma")))
        return JsonResponse(request, safe=False, status=200)

def sumal(request):
    if request.method== "GET":
        q = Actions.objects.filter(id).only('suma')
        return render (request, 'ORTHF.html')

def home_screen_view(request):
    return render(request, "base.html",{})

def student_list(request):
    posts= Actions.objects.filter(suma=20).only('action')
    print(posts)
    print(connection.queries)
    return render(request, 'base.html', {'posts':posts})

def student_lists(request):
    posts= list(Actions.objects.filter(suma=20).values_list('action'))
    json.dumps(posts)
    print(connection.queries)
    return render(request, 'base.html', {'posts':posts})

def 
