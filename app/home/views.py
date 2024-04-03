from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from prediction import *
import numpy as np
def home(request):
    return render(request, 'home.html', {'cost': None})

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        sex = request.POST.get('sex')
        bmi=int(request.POST.get('bmi'))
        children=int(request.POST.get('children'))
        smoker=request.POST.get('smoker')
        region=request.POST.get('region')
        arr=[age,sex,bmi,children,smoker,region]
        cost=int(make_predictions(arr))
        return render(request, 'home.html', {'cost': cost})
    else:
        return HttpResponse("Method not allowed")
